# Description
Testing the mapping between ChEBI and PubChem identifiers.

# Code
```
indra.databases import chebi_client
indra.util import unicode_strs

def test_chebi_pubchem_mapping():
    # This is a non-trivial mapping since there are multiple mappings
    # reported by ChEBI and we need to choose the right one based on
    # InChIKey matches.
    assert chebi_client.get_chebi_id_from_pubchem('5287993') == 'CHEBI:3528'

```
