# Description
Test the get_stmt_type function to map strings to statement types.

# Code
```

def test_get_stmt_type():
    assert get_stmt_type('CATALYSIS').__name__ == 'Activation'
    assert get_stmt_type('INHIBITION').__name__ == 'Inhibition'
    assert get_stmt_type('HETERODIMER_ASSOCIATION').__name__ == 'Complex'
    assert get_stmt_type('CATALYSIS;HETERODIMER_ASSOCIATION').__name__ == \
           'Complex'

```
