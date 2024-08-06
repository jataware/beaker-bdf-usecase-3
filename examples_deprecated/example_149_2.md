# Description
Example of loading prior statements from a pickle file into an `IncrementalModel`.

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

    def load_prior(self, prior_fname):
        """Load a set of prior statements from a pickle file.

        The prior statements have a special key in the stmts dictionary
        called "prior".

        Parameters
        ----------
        prior_fname : str
            The name of the pickle file containing the prior Statements.
        """

```
