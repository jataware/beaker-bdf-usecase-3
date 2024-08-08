# Description
This example demonstrates various quantitative conversions such as converting units of time and rate, and handling conversion with target periods.

# Code
```
from indra.statements.delta import QuantitativeState

def test_quantitative_conversions():
    day = QuantitativeState._get_period_from_unit('day')
    assert QuantitativeState.value_per_second(86400, day) == 1
    assert QuantitativeState.from_seconds(1, day) == 86400
    qs1 = QuantitativeState(value=86400, unit='day')
    qs2 = QuantitativeState(value=302400, unit='week')
    values = qs1._standardize_units(qs2, target_unit='second')
    assert values[0] == 1.0  # 86400 / 86400 sec/day
    assert values[1] == 0.5  # 302400 / 604800 sec/week
    # Convert between different rates
    assert QuantitativeState.convert_unit('day', 'week', 10) == 70
    assert QuantitativeState.convert_unit('week', 'day', 21) == 3
    # Use given periods versus approximate values
    jan = date(2019, 2, 1) - date(2019, 1, 1)
    feb = date(2019, 3, 1) - date(2019, 2, 1)
    feb_leap = date(2016, 3, 1) - date(2016, 2, 1)
    assert QuantitativeState.convert_unit(
        'day', 'month', 1, target_period=jan) == 31
    assert QuantitativeState.convert_unit(
        'day', 'month', 1, target_period=feb) == 28
    assert QuantitativeState.convert_unit(
        'day', 'month', 1, target_period=feb_leap) == 29
    assert QuantitativeState.convert_unit('day', 'month', 1) == 30
    # Convert to absolute value
    abs_period = timedelta(weeks=5)
    assert QuantitativeState.convert_unit(
        'day', 'absolute', 2, day, abs_period) == 70
    assert QuantitativeState.convert_unit(
        'week', 'absolute', 25, target_period=abs_period) == 125
    # Get rate from absolute value
    assert QuantitativeState.convert_unit(
        'absolute', 'day', 70, source_period=abs_period) == 2
    assert QuantitativeState.convert_unit(
        'absolute', 'week', 70, source_period=abs_period) == 14
    # Convert to or from absolute value without providing a total period
    with pytest.raises(ValueError):
        QuantitativeState.convert_unit('absolute', 'week', 70)
    with pytest.raises(ValueError):

```
