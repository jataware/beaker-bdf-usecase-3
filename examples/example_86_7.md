# Description
Test case for checking 'is_a' relationships of a GO term.

# Code
```

def test_isa():
    rel = set(go_client._client.entries['GO:0001671']['relations']['is_a'])

```
