# Description
This example shows how to create an `Agent` instance with a specified activity state, using the `ActivityCondition` class. The first example shows an Agent (`MAP2K1`) with kinase activity set to active. The second example shows an Agent (`FOXO3`) with transcriptional activity set to inactive.

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

class ActivityCondition(object):
    def __init__(self, activity_type, is_active):
        if activity_type not in activity_types:
            logger.warning('Invalid activity type: %s' % activity_type)
        self.activity_type = activity_type

    >>> mek_active = Agent('MAP2K1',
    ...                    activity=ActivityCondition('kinase', True))

    Transcriptionally inactive FOXO3:

    >>> foxo_inactive = Agent('FOXO3',

```
