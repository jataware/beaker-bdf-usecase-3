# Description
This example demonstrates how to serialize a `QualitativeDelta` object to JSON and verify its contents.

# Code
```

def test_qualitative_serialization():
    qd = QualitativeDelta(polarity=1, adjectives=['strong', 'significant'])
    qdj = qd.to_json()
    assert qdj['type'] == 'qualitative'
    assert qdj['polarity'] == 1
    assert qdj['adjectives'] == ['strong', 'significant']

```
