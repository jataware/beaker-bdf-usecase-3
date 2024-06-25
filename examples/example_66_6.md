# Description
Testing retrieval of ChEBI names from the web given ChEBI identifiers.

# Code
```
indra.databases import chebi_client
indra.util import unicode_strs

def test_chebi_name_from_web():
    name = chebi_client.get_chebi_name_from_id_web('63637')
    assert name == 'vemurafenib'
    name = chebi_client.get_chebi_name_from_id_web('44215')

```
