# Description
Test case for validating and retrieving a GO location using different identifier forms.

# Code
```

def test_get_valid_location():
    assert go_client.get_valid_location('0001669') == 'acrosomal vesicle'
    assert go_client.get_valid_location('GO:0001669') == 'acrosomal vesicle'
    assert go_client.get_valid_location('acrosomal vesicle') == \
        'acrosomal vesicle'

```
