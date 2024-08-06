# Description
This example demonstrates how to compare different `QualitativeDelta` objects and check for equality and opposition.

# Code
```

def test_qualitative_delta_comparisons():
    qd1 = QualitativeDelta(polarity=1, adjectives=['strong', 'significant'])
    qd2 = QualitativeDelta(polarity=1, adjectives=['strong', 'significant'])
    qd3 = QualitativeDelta(polarity=-1, adjectives=['strong', 'significant'])
    qd4 = QualitativeDelta(polarity=1, adjectives=['weak', 'insignificant'])
    qd5 = QualitativeDelta(polarity=None, adjectives=None)
    assert qd1.equals(qd2)
    assert not qd1.equals(qd3)
    assert not qd1.equals(qd4)
    assert qd1.is_opposite(qd3)
    assert not qd1.is_opposite(qd5)

```
