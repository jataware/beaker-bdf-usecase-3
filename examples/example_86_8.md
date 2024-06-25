# Description
Test case for retrieving xrefs of a GO term.

# Code
```

def test_xrefs():
    xr = go_client._client.entries['GO:0008463']['xrefs']['KEGG_REACTION']

```
