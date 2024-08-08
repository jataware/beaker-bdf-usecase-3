# Description
Test case for looking up the label of a GO term using its ID.

# Code
```

def test_go_id_lookup():
    go_id = 'GO:0001768'
    go_name = go_client.get_go_label(go_id)

```
