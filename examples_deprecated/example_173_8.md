# Description
Add cross-references (xrefs) within Famplex entities.

# Code
```
from indra.util import read_unicode_csv

def add_famplex_xrefs(self):
    edges = []
    include_refs = {'PF', 'IP', 'GO', 'NCIT', 'ECCODE', 'HGNC_GROUP',
                    'MESH'}
    for row in read_unicode_csv(get_resource_path('famplex_map.tsv'),
                                delimiter='\t'):
        ref_ns, ref_id, fplx_id = row
        if ref_ns not in include_refs:
            continue
        edges.append((self.label(ref_ns, ref_id),
                      self.label('FPLX', fplx_id),
                      {'type': 'xref', 'source': 'fplx'}))
        # We avoid FPLX->MESH mappings in this direction due to
        # species-specificity issues
        if ref_ns != 'MESH':
            edges.append((self.label('FPLX', fplx_id),
                          self.label(ref_ns, ref_id),
                          {'type': 'xref', 'source': 'fplx'}))

```
