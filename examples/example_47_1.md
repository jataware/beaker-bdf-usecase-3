# Description
This example demonstrates how to create an `Agent` instance with bound conditions, using the `BoundCondition` class. The first Agent (`EGFR`) is bound to another Agent (`EGF`), and the second Agent (`BRAF`) is bound with a condition specifying that it is not bound to another Agent (`YWHAB`).

# Code
```
from collections import OrderedDict as _o
from indra.statements.statements import modtype_conditions, modtype_to_modclass
from .concept import Concept
from .resources import get_valid_residue, activity_types, amino_acids
import logging

logger = logging.getLogger(__name__)

default_ns_order = ['FPLX', 'UPPRO', 'HGNC', 'UP', 'CHEBI', 'GO', 'MESH', 'MIRBASE', 'DOID', 'HP', 'EFO']

class Agent(Concept):
    def __init__(self, name, mods=None, activity=None, bound_conditions=None, mutations=None, location=None, db_refs=None):
        super(Agent, self).__init__(name, db_refs=db_refs)
        self.mods = [] if mods is None else ([mods] if isinstance(mods, ModCondition) else mods)
        self.bound_conditions = [] if bound_conditions is None else ([bound_conditions] if isinstance(bound_conditions, BoundCondition) else bound_conditions)
        self.mutations = [] if mutations is None else ([mutations] if isinstance(mutations, MutCondition) else mutations)
        self.activity = activity
        self.location = location

class BoundCondition(object):
    def __init__(self, agent, is_bound=True):
        self.agent = agent

    >>> egf = Agent('EGF')
    >>> egfr = Agent('EGFR', bound_conditions=[BoundCondition(egf)])

    BRAF *not* bound to a 14-3-3 protein (YWHAB):

    >>> ywhab = Agent('YWHAB')
    >>> braf = Agent('BRAF', bound_conditions=[BoundCondition(ywhab, False)])

```
