# Description
Test case for retrieving a GO ID from a label or synonym.

# Code
```

def test_id_from_label_or_synonym():
    assert go_client.get_go_id_from_label_or_synonym(
        'amoeboidal cell migration') == 'GO:0001667'
    assert go_client.get_go_id_from_label_or_synonym(

```
