# Description
Score paths by comparing them to a set of agent values.

# Code
```

    def score_paths(self, paths, agents_values, loss_of_function=False,
                    sigma=0.15, include_final_node=False):
        """Return scores associated with a given set of paths.

        Parameters
        ----------
        paths : list[list[tuple[str, int]]]
            A list of paths obtained from path finding. Each path is a list
            of tuples (which are edges in the path), with the first element
            of the tuple the name of a rule, and the second element its
            polarity in the path.
        agents_values : dict[indra.statements.Agent, float]
            A dictionary of INDRA Agents and their corresponding measured
            value in a given experimental condition.
        loss_of_function : Optional[boolean]
            If True, flip the polarity of the path. For instance, if the effect
            of an inhibitory drug is explained, set this to True.
            Default: False
        sigma : Optional[float]
            The estimated standard deviation for the normally distributed
            measurement error in the observation model used to score paths
            with respect to data. Default: 0.15
        include_final_node : Optional[boolean]
            Determines whether the final node of the path is included in the
            score. Default: False
        """
        obs_model = lambda x: scipy.stats.norm(x, sigma)
        # Build up dict mapping observables to values
        obs_dict = {}
        for ag, val in agents_values.items():
            obs_list = self.agent_to_obs[ag]
            if obs_list is not None:
                for obs in obs_list:
                    obs_dict[obs] = val
        # For every path...
        path_scores = []
        for path in paths:
            logger.info('------')
            logger.info("Scoring path:")
            logger.info(path)
            # Look at every node in the path, excluding the final
            # observable...
            path_score = 0
            last_path_node_index = -1 if include_final_node else -2
            for node, sign in path[:last_path_node_index]:
                # ...and for each node check the sign to see if it matches the
                # data. So the first thing is to look at what's downstream
                # of the rule
                # affected_obs is a list of observable names alogn
                for affected_obs, rule_obs_sign in self.rule_obs_dict[node]:
                    flip_polarity = -1 if loss_of_function else 1
                    pred_sign = sign * rule_obs_sign * flip_polarity
                    # Check to see if this observable is in the data
                    logger.info('%s %s: effect %s %s' %
                                (node, sign, affected_obs, pred_sign))
                    measured_val = obs_dict.get(affected_obs)
                    if measured_val:
                        # For negative predictions use CDF (prob that given
                        # measured value, true value lies below 0)
                        if pred_sign <= 0:
                            prob_correct = obs_model(measured_val).logcdf(0)
                        # For positive predictions, use log survival function
                        # (SF = 1 - CDF, i.e., prob that true value is
                        # above 0)
                        else:
                            prob_correct = obs_model(measured_val).logsf(0)
                        logger.info('Actual: %s, Log Probability: %s' %
                                    (measured_val, prob_correct))
                        path_score += prob_correct
                if not self.rule_obs_dict[node]:
                    logger.info('%s %s' % (node, sign))
                    prob_correct = obs_model(0).logcdf(0)
                    logger.info('Unmeasured node, Log Probability: %s' %
                                (prob_correct))
                    path_score += prob_correct
            # Normalized path
            # path_score = path_score / len(path)
            logger.info("Path score: %s" % path_score)
            path_scores.append(path_score)
        path_tuples = list(zip(paths, path_scores))
        # Sort first by path length
        sorted_by_length = sorted(path_tuples, key=lambda x: len(x[0]))
        # Sort by probability; sort in reverse order to large values
        # (higher probabilities) are ranked higher
        scored_paths = sorted(sorted_by_length, key=lambda x: x[1],
                              reverse=True)

```
