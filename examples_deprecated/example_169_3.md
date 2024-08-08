# Description
Retrieve the influence map for the model, generating it if necessary.

# Code
```

    def get_im(self, force_update=False):
        """Get the influence map for the model, generating it if necessary.

        Parameters
        ----------
        force_update : bool
            Whether to generate the influence map when the function is called.
            If False, returns the previously generated influence map if
            available. Defaults to True.

        Returns
        -------
        networkx MultiDiGraph object containing the influence map.
            The influence map can be rendered as a pdf using the dot layout
            program as follows::

                im_agraph = nx.nx_agraph.to_agraph(influence_map)
                im_agraph.draw('influence_map.pdf', prog='dot')
        """
        if self._im and not force_update:
            return self._im
        if not self.model:
            raise Exception("Cannot get influence map if there is no model.")

        def add_obs_for_agents(main_agent, ref_agents=None):
            if ref_agents:
                all_agents = [main_agent] + ref_agents
            else:
                all_agents = [main_agent]
            ag_to_obj_mps = self.get_all_mps(all_agents, mapping=True)
            if all([not v for v in ag_to_obj_mps.values()]):
                logger.debug('No monomer patterns found in model for agents %s'
                             ', skipping' % all_agents)
                return
            obs_nodes = NodesContainer(main_agent, ref_agents)
            main_obs_set = set()
            ref_obs_set = set()
            for agent in ag_to_obj_mps:
                for obj_mp in ag_to_obj_mps[agent]:
                    obs_name = _monomer_pattern_label(obj_mp) + '_obs'
                    self.obs_to_agents[obs_name] = agent
                    # Add the observable
                    obj_obs = Observable(obs_name, obj_mp, _export=False)
                    if agent.matches(main_agent):
                        main_obs_set.add(obs_name)
                    else:
                        ref_obs_set.add(obs_name)
                    try:
                        self.model.add_component(obj_obs)
                        self.model.add_annotation(
                            Annotation(obs_name, agent.name,
                                       'from_indra_agent'))
                    except ComponentDuplicateNameError as e:
                        pass
            obs_nodes.main_interm = main_obs_set
            obs_nodes.ref_interm = ref_obs_set
            return obs_nodes

        # Create observables for all statements to check, and add to model
        # Remove any existing observables in the model
        self.model.observables = ComponentSet([])
        for stmt in self.statements:
            # Generate observables for Modification statements
            if isinstance(stmt, Modification) or \
               isinstance(stmt, SelfModification):
                # If the statement is a regular Mod, the target is stmt.sub
                if isinstance(stmt, Modification):
                    sub = stmt.sub
                # If it's a SelfMod, the target is stmt.enz
                elif isinstance(stmt, SelfModification):
                    sub = stmt.enz
                # Add the mod for the agent
                if sub is None:
                    self.stmt_to_obs[stmt] = NodesContainer(None)
                else:
                    mod_condition_name = modclass_to_modtype[stmt.__class__]
                    if isinstance(stmt, RemoveModification):
                        mod_condition_name = modtype_to_inverse[
                            mod_condition_name]
                    # Add modification to substrate agent
                    modified_sub = _add_modification_to_agent(
                            sub, mod_condition_name, stmt.residue,
                            stmt.position)
                    # Get all refinements of substrate agent
                    ref_subs = self.get_refinements(modified_sub)
                    obs_nodes = add_obs_for_agents(modified_sub, ref_subs)
                    # Associate this statement with this observable
                    self.stmt_to_obs[stmt] = obs_nodes
            # Generate observables for Activation/Inhibition statements
            elif isinstance(stmt, RegulateActivity):
                if stmt.obj is None:
                    self.stmt_to_obs[stmt] = NodesContainer(None)
                else:
                    # Add activity to object agent
                    regulated_obj = _add_activity_to_agent(
                        stmt.obj, stmt.obj_activity, stmt.is_activation)
                    # Get all refinements of object agent
                    ref_objs = self.get_refinements(stmt.obj)
                    obs_nodes = add_obs_for_agents(regulated_obj, ref_objs)
                    # Associate this statement with this observable
                    self.stmt_to_obs[stmt] = obs_nodes
            elif isinstance(stmt, RegulateAmount):
                if stmt.obj is None:
                    self.stmt_to_obs[stmt] = NodesContainer(None)
                else:
                    # Get all refinements of object agent
                    ref_objs = self.get_refinements(stmt.obj)
                    obs_nodes = add_obs_for_agents(stmt.obj, ref_objs)
                    self.stmt_to_obs[stmt] = obs_nodes
            elif isinstance(stmt, Influence):
                if stmt.obj is None:
                    self.stmt_to_obs[stmt] = NodesContainer(None)
                else:
                    # Get all refinements of object agent
                    ref_objs = self.get_refinements(stmt.obj)
                    concepts = [obj.concept for obj in ref_objs]
                    obs_nodes = add_obs_for_agents(stmt.obj.concept, concepts)
                    self.stmt_to_obs[stmt] = obs_nodes
        # Add observables for each agent
        for ag in self.agent_obs:
            obs_nodes = add_obs_for_agents(ag)
            self.agent_to_obs[ag] = obs_nodes

        logger.info("Generating influence map")
        self._im = self.generate_im(self.model)
        # self._im.is_multigraph = lambda: False
        # Now, for every rule in the model, check if there are any observables
        # downstream; alternatively, for every observable in the model, get a
        # list of rules.
        # We'll need the dictionary to check if nodes are observables
        node_attributes = nx.get_node_attributes(self._im, 'node_type')
        for rule in self.model.rules:
            obs_list = []
            # Get successors of the rule node
            for neighb in self._im.neighbors(rule.name):
                # Check if the node is an observable
                if node_attributes[neighb] != 'variable':
                    continue
                # Get the edge and check the polarity
                edge_sign = _get_edge_sign(self._im, (rule.name, neighb))
                obs_list.append((neighb, edge_sign))
            self.rule_obs_dict[rule.name] = obs_list

```
