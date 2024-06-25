# Description
How to run Gilda disambiguation on an Agent in an INDRA Statement.

# Code
```
import logging
from indra.config import get_config, has_config
import standardize_agent_name
from indra.ontology.standardize import standardize_agent_name

    def run_gilda_disambiguation(self, stmt, agent, idx, agent_txt,
                                 mode='web'):
        """Run Gilda disambiguation on an Agent in a given Statement.

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
        mode : Optional[str]
            If 'web', the web service given in the GILDA_URL config setting or
            environmental variable is used. Otherwise, the gilda package is
            attempted to be imported and used. Default: web

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
        # Initialize annotations if needed so predicted
        # probabilities can be added to Agent annotations
        annots = stmt.evidence[0].annotations
        if 'agents' in annots:
            if 'gilda' not in annots['agents']:
                annots['agents']['gilda'] = \
                    [None for _ in stmt.agent_list()]
        else:
            annots['agents'] = {'gilda': [None for _ in stmt.agent_list()]}
        grounding_text = self._get_text_for_grounding(stmt, agent_txt)
        if grounding_text:
            gilda_result = ground_agent(agent, agent_txt, grounding_text, mode)
            if gilda_result:
                logger.debug('Disambiguated %s to: %s' %
                             (agent_txt, agent.name))
                annots['agents']['gilda'][idx] = gilda_result
                success = True

```
