# Description
How to run Adeft disambiguation on an Agent in an INDRA Statement.

# Code
```
import logging
from indra.config import get_config, has_config
from indra.ontology.standardize import standardize_agent_name
try:
    from adeft import available_shortforms as available_adeft_models
    from adeft.disambiguate import load_disambiguator
    adeft_disambiguators = {}
    for shortform in available_adeft_models:
        adeft_disambiguators[shortform] = load_disambiguator(shortform)
except Exception:
    logging.getLogger(__name__).info('Adeft will not be available for grounding disambiguation.')

    def run_adeft_disambiguation(self, stmt, agent, idx, agent_txt):
        """Run Adeft disambiguation on an Agent in a given Statement.

        This function looks at the evidence of the given Statement and attempts
        to look up the full paper or the abstract for the evidence. If both of
        those fail, the evidence sentence itself is used for disambiguation.
        The disambiguation model corresponding to the Agent text is then
        called, and the highest scoring returned grounding is set as the
        Agent's new grounding.

        The Statement's annotations as well as the Agent are modified in place
        and no value is returned.

        Parameters
        ----------
        stmt : indra.statements.Statement
            An INDRA Statement in which the Agent to be disambiguated appears.
        agent : indra.statements.Agent
            The Agent (potentially grounding mapped) which we want to
            disambiguate in the context of the evidence of the given Statement.
        idx : int
            The index of the new Agent's position in the Statement's agent list
            (needed to set annotations correctly).

        Returns
        -------
        bool
            True if disambiguation was successfully applied, and False
            otherwise.  Reasons for a False response can be the lack of
            evidence as well as failure to obtain text for grounding
            disambiguation.
        """
        success = False
        # If the Statement doesn't have evidence for some reason, then there is
        # no text to disambiguate by
        # NOTE: we might want to try disambiguating by other agents in the
        # Statement
        if not stmt.evidence:
            return False
        # Initialize annotations if needed so Adeft predicted
        # probabilities can be added to Agent annotations
        annots = stmt.evidence[0].annotations
        if 'agents' in annots:
            if 'adeft' not in annots['agents']:
                annots['agents']['adeft'] = \
                    {'adeft': [None for _ in stmt.agent_list()]}
        else:
            annots['agents'] = {'adeft': [None for _ in stmt.agent_list()]}
        grounding_text = self._get_text_for_grounding(stmt, agent_txt)

        def apply_grounding(agent, agent_txt, ns_and_id):
            db_ns, db_id = ns_and_id.split(':', maxsplit=1)
            if db_ns == 'CHEBI' and not db_id.startswith('CHEBI:'):
                db_id = 'CHEBI:%s' % db_id
            agent.db_refs = {'TEXT': agent_txt, db_ns: db_id}
            agent.name = standard_name
            logger.debug('Disambiguated %s to: %s, %s:%s' %
                         (agent_txt, standard_name, db_ns, db_id))
            standardize_agent_name(agent, standardize_refs=True)

        def remove_grounding(agent, agent_txt):
            agent.name = agent_txt
            agent.db_refs = {'TEXT': agent_txt}

        if grounding_text:
            da = adeft_disambiguators[agent_txt]
            res = da.disambiguate([grounding_text])
            ns_and_id, standard_name, disamb_scores = res[0]
            # If grounding with highest score is not a positive label we
            # explicitly remove grounding and reset the (potentially incorrectly
            # standardized) name to the original text value.
            # Ungrounded labels will lack a ':', an ungrounded label should
            # never be a pos_label but we still check both if the label is
            # positive and if it contains ':' for the sake of caution since
            # pos_labels are determined by manual review.
            # Otherwise if the Adeft model's precision for that particular
            # grounding is greater than or equal to 0.5 or if there is a
            # defining pattern for the ambiguous shortform in the text we
            # update the db_refs with what we got from Adeft and set the
            # standard name.
            if ':' in ns_and_id and ns_and_id in da.pos_labels:
                # Determine the precision associated with the given grounding
                stats = da.classifier.stats
                if stats and ns_and_id in stats:
                    precision = stats[ns_and_id]['pr']['mean']
                # If there is no precision info, we fall back to a value that
                # is < 0.5.
                else:
                    precision = .499
                # With high enough precision or a defining pattern, we accept
                # the grounding and set it.
                if precision >= 0.5 or disamb_scores[ns_and_id] == 1:
                    apply_grounding(agent, agent_txt, ns_and_id)
                    annots['agents']['adeft'][idx] = disamb_scores
                # Otherwise we remove any prior grounding.
                else:
                    remove_grounding(agent, agent_txt)
            # In this case the entity is either ungrounded or not a positive
            # label so we remove any prior grounding.
            else:
                remove_grounding(agent, agent_txt)
            success = True

```
