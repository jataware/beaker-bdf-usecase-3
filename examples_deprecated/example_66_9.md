# Description
Testing the retrieval of primary ChEBI identifiers given secondary identifiers.

# Code
```
indra.databases import chebi_client
indra.util import unicode_strs

def test_chebi_to_primary():
    assert chebi_client.get_primary_id('CHEBI:6281') == 'CHEBI:17490'

```
