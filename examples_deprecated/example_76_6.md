# Description
This example demonstrates performing arithmetic operations on `QuantitativeState` objects, including addition, subtraction, comparisons, and handling operations with different units and entities.

# Code
```

def test_arithmetic_operations():
    qs1 = QuantitativeState('person', 15, 'day')
    qs2 = QuantitativeState('person', 10, 'day')
    qs3 = QuantitativeState('person', 100, 'week')
    qs4 = QuantitativeState('person', 70, 'week')
    qs5 = QuantitativeState('box', 100, 'day')
    qs6 = QuantitativeState('person', 100, 'absolute')
    qs7 = QuantitativeState('person', 30, 'absolute')
    day = QuantitativeState._get_period_from_unit('day')
    # Operations with the same entity and unit
    assert qs1 + qs2 == (25, 'day'), qs1 + qs2
    assert qs1 - qs2 == (5, 'day'), qs1 - qs2
    assert qs1 > qs2
    assert qs2 < qs1
    assert qs1 != qs2
    # Operations with absolute values
    assert qs6 + qs7 == (130, 'absolute')
    assert qs6 - qs7 == (70, 'absolute')
    assert qs6 > qs7
    assert qs7 < qs6
    # Operations with different units
    sum_per_second = (qs1 + qs4)[0]
    sum_per_day = QuantitativeState.from_seconds(sum_per_second, day)
    assert sum_per_day == 25, sum_per_day
    diff_per_second = (qs1 - qs4)[0]
    diff_per_day = QuantitativeState.from_seconds(diff_per_second, day)
    assert diff_per_day == 5, diff_per_day
    assert qs1 > qs4
    assert qs2 < qs3
    assert qs2 == qs4
    assert qs1 != qs3
    # Operations with different entities
    with pytest.raises(ValueError):
        qs1 + qs5
    # Operations with absolute unit when absolute period not provided
    with pytest.raises(ValueError):

```
