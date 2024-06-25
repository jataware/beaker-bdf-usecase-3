# Description
Testing the mapping between ChEBI and ChEMBL identifiers.

# Code
```
indra.databases import chebi_client
indra.util import unicode_strs

def test_chebi_chembl():
    assert chebi_client.get_chebi_id_from_chembl('CHEMBL525191') == \
        'CHEBI:83405'

```
