# Description
This example demonstrates how to create an `Agent` instance with specific post-translational modifications, using the `ModCondition` class. The first example shows an Agent (`MAP2K1`) with two phosphorylation modifications. The second example shows an Agent (`MAPK1`) which is unphosphorylated at a specific position.

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

class ModCondition(object):
    def __init__(self, mod_type, residue=None, position=None, is_modified=True):
        if mod_type not in modtype_conditions:
            logger.warning('Unknown modification type: %s' % mod_type)
        self.mod_type = mod_type
        self.residue = get_valid_residue(residue)
        self.position = str(position) if isinstance(position, int) else position

    >>> phospho_mek = Agent('MAP2K1', mods=[
    ... ModCondition('phosphorylation', 'S', '202'),
    ... ModCondition('phosphorylation', 'S', '204')])

    ERK (MAPK1) unphosphorylated at tyrosine 187:

    >>> unphos_erk = Agent('MAPK1', mods=(

```
