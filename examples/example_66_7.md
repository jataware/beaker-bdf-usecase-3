# Description
Testing retrieval of InChIKey given ChEBI identifiers.

# Code
```
indra.databases import chebi_client
indra.util import unicode_strs

def test_inchi_key():
    ik = chebi_client.get_inchi_key('2150')

```
