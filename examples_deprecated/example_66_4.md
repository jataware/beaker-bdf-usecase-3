# Description
Testing retrieval of ChEBI names given ChEBI identifiers.

# Code
```
indra.databases import chebi_client
indra.util import unicode_strs

def test_chebi_id_to_name():
    name = chebi_client.get_chebi_name_from_id('CHEBI:63637')

```
