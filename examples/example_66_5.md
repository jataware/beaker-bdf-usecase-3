# Description
Testing retrieval of ChEBI identifiers given ChEBI names.

# Code
```
indra.databases import chebi_client
indra.util import unicode_strs

def test_chebi_name_to_id():
    cid = chebi_client.get_chebi_id_from_name('vemurafenib')

```
