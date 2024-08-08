# Description
Example of using the `IncrementalModel` to preassemble a set of INDRA statements with various filtering options.

# Code
```
import pickle
import logging
from indra.statements import Agent
import indra.tools.assemble_corpus as ac
from indra.databases import hgnc_client
from indra.ontology.bio import bio_ontology

logger = logging.getLogger(__name__)

class IncrementalModel(object):
    def __init__(self, model_fname=None):
        if model_fname is None:
            self.stmts = {}
        else:
            try:
                with open(model_fname, 'rb') as f:
                    self.stmts = pickle.load(f)
            except:
                logger.warning('Could not load %s, starting new model.' % model_fname)
                self.stmts = {}
        self.prior_genes = []
        self.assembled_stmts = []

    def save(self, model_fname='model.pkl'):
        with open(model_fname, 'wb') as fh:
            pickle.dump(self.stmts, fh, protocol=4)

    def add_statements(self, pmid, stmts):
        if pmid not in self.stmts:
            self.stmts[pmid] = stmts
        else:
            self.stmts[pmid] += stmts

    def _relevance_filter(self, stmts, filters=None):
        if filters is None:
            return stmts
        logger.info('Running relevance filter on %d statements' % len(stmts))
        prior_agents = get_gene_agents(self.prior_genes)
        if 'prior_all' in filters:
            stmts = _ref_agents_all_filter(stmts, prior_agents)
        elif 'prior_one' in filters:
            stmts = _ref_agents_one_filter(stmts, prior_agents)
        logger.info('%d statements after relevance filter' % len(stmts))
        return stmts

    def preassemble(self, filters=None, grounding_map=None):
        stmts = self.get_statements()

        stmts = ac.filter_no_hypothesis(stmts)

        if grounding_map is not None:
            stmts = ac.map_grounding(stmts, grounding_map=grounding_map)
        else:
            stmts = ac.map_grounding(stmts)

        if filters and ('grounding' in filters):
            stmts = ac.filter_grounded_only(stmts)

        stmts = ac.map_sequence(stmts)

        if filters and 'human_only' in filters:
            stmts = ac.filter_human_only(stmts)

        stmts = ac.run_preassembly(stmts, return_toplevel=False)

        stmts = self._relevance_filter(stmts, filters)


    def preassemble(self, filters=None, grounding_map=None):
        """Preassemble the Statements collected in the model.

        Use INDRA's GroundingMapper, Preassembler and BeliefEngine
        on the IncrementalModel and save the unique statements and
        the top level statements in class attributes.

        Currently the following filter options are implemented:
        - grounding: require that all Agents in statements are grounded
        - human_only: require that all proteins are human proteins
        - prior_one: require that at least one Agent is in the prior model
        - prior_all: require that all Agents are in the prior model

        Parameters
        ----------
        filters : Optional[list[str]]
            A list of filter options to apply when choosing the statements.
            See description above for more details. Default: None
        grounding_map : Optional[dict]
            A user supplied grounding map which maps a string to a
            dictionary of database IDs (in the format used by Agents'
            db_refs).
        """
        stmts = self.get_statements()

        # Filter out hypotheses
        stmts = ac.filter_no_hypothesis(stmts)

        # Fix grounding
        if grounding_map is not None:
            stmts = ac.map_grounding(stmts, grounding_map=grounding_map)
        else:
            stmts = ac.map_grounding(stmts)

        if filters and ('grounding' in filters):
            stmts = ac.filter_grounded_only(stmts)

        # Fix sites
        stmts = ac.map_sequence(stmts)

        if filters and 'human_only' in filters:
            stmts = ac.filter_human_only(stmts)

        # Run preassembly
        stmts = ac.run_preassembly(stmts, return_toplevel=False)

        # Run relevance filter
        stmts = self._relevance_filter(stmts, filters)

        # Save Statements

```
