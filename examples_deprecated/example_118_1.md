# Description
Use the `get_inchi_key` method from the Pubchem client to retrieve the InChI key for a given PubChem compound ID.

# Code
```

def test_get_inchi_key():
    ik = pubchem_client.get_inchi_key('5280613')

```
