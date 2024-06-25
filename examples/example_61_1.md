# Description
Example of using the `biolookup_client.lookup_curie` function to look up the name of a compound using a CURIE.

# Code
```

def test_lookup_curie():
    curie = 'pubchem.compound:40976'
    res = biolookup_client.lookup_curie(curie)
    assert res['name'] == '(17R)-13-ethyl-17-ethynyl-17-hydroxy-11-' \
        'methylidene-2,6,7,8,9,10,12,14,15,16-decahydro-1H-' \

```
