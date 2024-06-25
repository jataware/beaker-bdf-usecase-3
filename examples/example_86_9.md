# Description
Test case for checking the namespace of various GO terms.

# Code
```

def test_namespace():
    assert go_client.get_namespace('xxx') is None
    assert go_client.get_namespace('GO:0000015') == 'cellular_component'
    assert go_client.get_namespace('GO:0000017') == 'biological_process'

```
