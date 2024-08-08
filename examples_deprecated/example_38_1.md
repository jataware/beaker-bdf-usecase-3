# Description
Fixing site errors on both the modification state of an agent (MAP2K1) and the target of a Phosphorylation statement (MAPK1).

# Code
```
import logging
import textwrap
from copy import deepcopy
from functools import lru_cache
from protmapper.api import ProtMapper, default_site_map
from indra.statements import *
from indra.databases import hgnc_client

logger = logging.getLogger(__name__)

class MappedStatement(object):
    # Class definition...

class SiteMapper(ProtMapper):
    # Class definition...


default_mapper = SiteMapper(default_site_map)

@lru_cache(maxsize=10000)
def _get_uniprot_id(agent):
    # Function definition...

def _valid_position_str(pos):

    >>> map2k1_phos = Agent('MAP2K1', db_refs={'UP':'Q02750'}, mods=[
    ... ModCondition('phosphorylation', 'S', '217'),
    ... ModCondition('phosphorylation', 'S', '221')])
    >>> mapk1 = Agent('MAPK1', db_refs={'UP':'P28482'})
    >>> stmt = Phosphorylation(map2k1_phos, mapk1, 'T','183')
    >>> (valid, mapped) = default_mapper.map_sites([stmt])
    >>> valid
    []
    >>> mapped
    [
    MappedStatement:
        original_stmt: Phosphorylation(MAP2K1(mods: (phosphorylation, S, 217), (phosphorylation, S, 221)), MAPK1(), T, 183)
        mapped_mods: MappedSite(up_id='Q02750', error_code=None, valid=False, orig_res='S', orig_pos='217', mapped_id='Q02750', mapped_res='S', mapped_pos='218', description='off by one', gene_name='MAP2K1')
                     MappedSite(up_id='Q02750', error_code=None, valid=False, orig_res='S', orig_pos='221', mapped_id='Q02750', mapped_res='S', mapped_pos='222', description='off by one', gene_name='MAP2K1')
                     MappedSite(up_id='P28482', error_code=None, valid=False, orig_res='T', orig_pos='183', mapped_id='P28482', mapped_res='T', mapped_pos='185', description='INFERRED_MOUSE_SITE', gene_name='MAPK1')
        mapped_stmt: Phosphorylation(MAP2K1(mods: (phosphorylation, S, 218), (phosphorylation, S, 222)), MAPK1(), T, 185)
    ]
    >>> ms = mapped[0]
    >>> ms.original_stmt
    Phosphorylation(MAP2K1(mods: (phosphorylation, S, 217), (phosphorylation, S, 221)), MAPK1(), T, 183)
    >>> ms.mapped_mods
    [MappedSite(up_id='Q02750', error_code=None, valid=False, orig_res='S', orig_pos='217', mapped_id='Q02750', mapped_res='S', mapped_pos='218', description='off by one', gene_name='MAP2K1'), MappedSite(up_id='Q02750', error_code=None, valid=False, orig_res='S', orig_pos='221', mapped_id='Q02750', mapped_res='S', mapped_pos='222', description='off by one', gene_name='MAP2K1'), MappedSite(up_id='P28482', error_code=None, valid=False, orig_res='T', orig_pos='183', mapped_id='P28482', mapped_res='T', mapped_pos='185', description='INFERRED_MOUSE_SITE', gene_name='MAPK1')]
    >>> ms.mapped_stmt

```
