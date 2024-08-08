# Description
Testing the conversion from HMDB to ChEBI identifiers.

# Code
```
indra.databases import chebi_client
indra.util import unicode_strs

def test_hmdb_to_chebi():
    chebi_id = chebi_client.get_chebi_id_from_hmdb('HMDB0000122')

```
