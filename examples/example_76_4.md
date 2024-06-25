# Description
This example demonstrates how to serialize a `QuantitativeState` object to JSON and verify its contents.

# Code
```

def test_quantitative_serialization():
    qs = QuantitativeState('person', 100, 'absolute', 'more than',
                           'More than 100 people arrived to Ethiopia.', 1)
    qsj = qs.to_json()
    assert qsj['type'] == 'quantitative'
    assert qsj['entity'] == 'person', qsj['entity']
    assert qsj['value'] == 100, qsj['value']
    assert qsj['unit'] == 'absolute', qsj['unit']
    assert qsj['modifier'] == 'more than', qsj['modifier']
    assert qsj['polarity'] == 1

```
