# Description
Load PubChem CID to MeSH ID mappings from a TSV file.

# Code
```
from indra.resources import get_resource_path

def _load_pubchem_mesh_map():
    rows = read_unicode_csv(get_resource_path('pubchem_mesh_map.tsv'),
                            delimiter='\t')
    mappings = {row[0]: row[1] for row in rows}

```
