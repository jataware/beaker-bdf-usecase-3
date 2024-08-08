# Description
Testing the conversion of CAS numbers to ChEBI identifiers.

# Code
```
indra.databases import chebi_client
indra.util import unicode_strs

def test_cas_to_chebi():
    assert chebi_client.get_chebi_id_from_cas('23261-20-3') == 'CHEBI:18035'
    assert chebi_client.get_chebi_id_from_cas('100-51-6') == 'CHEBI:17987'

```
