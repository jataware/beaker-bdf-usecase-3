# Description
This example demonstrates how to set and change parameters in a `QualitativeDelta` object, such as polarity and adjectives.

# Code
```

def test_change_parameters():
    qd = QualitativeDelta(polarity=None, adjectives=None)
    assert qd.polarity is None
    assert qd.adjectives == []
    # Set polarity
    qd.set_polarity(1)
    assert qd.polarity == 1
    qd.set_polarity(-1)
    assert qd.polarity == -1
    qd.set_polarity(None)
    assert qd.polarity is None
    # Add adjectives
    qd.add_adjectives(['strong'])
    assert qd.adjectives == ['strong']
    qd.add_adjectives(['significant', 'severe'])

```
