# Description
Creating RunnableArgument instances with arguments and keyword arguments, and converting them to JSON.

# Code
```
from indra.pipeline import RunnableArgument
try:
    from indra_world.belief import get_eidos_bayesian_scorer
    has_indra_world = True
except ImportError:

@unittest.skipUnless(has_indra_world, 'indra_world not available')
def test_runnable_argument():
    # With args
    ra = RunnableArgument(
        get_eidos_bayesian_scorer,
        {'hume': [13, 7], 'cwms': [13, 7], 'sofia': [13, 7]})
    assert ra
    assert ra.func_name == 'get_eidos_bayesian_scorer'
    assert ra.args == ({'hume': [13, 7], 'cwms': [13, 7], 'sofia': [13, 7]}, )
    assert not ra.kwargs
    assert ra.to_json() == {
        'function': 'get_eidos_bayesian_scorer',
        'args': [{'hume': [13, 7], 'cwms': [13, 7], 'sofia': [13, 7]}]}
    # With kwargs
    ra = RunnableArgument(
        get_eidos_bayesian_scorer,
        prior_counts={'hume': [13, 7], 'cwms': [13, 7], 'sofia': [13, 7]})
    assert ra
    assert ra.func_name == 'get_eidos_bayesian_scorer'
    assert not ra.args
    assert ra.kwargs == {
        'prior_counts': {'hume': [13, 7], 'cwms': [13, 7], 'sofia': [13, 7]}}
    assert ra.to_json() == {
        'function': 'get_eidos_bayesian_scorer',
        'kwargs': {
            'prior_counts': {
                'hume': [13, 7], 'cwms': [13, 7], 'sofia': [13, 7]}}

```
