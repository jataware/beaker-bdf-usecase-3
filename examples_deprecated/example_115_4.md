# Description
Using the jsonify_arg_input function to convert arguments to JSON format.

# Code
```
from indra.pipeline.pipeline import jsonify_arg_input
try:
    from indra_world.assembly.matches import location_matches
    from indra.statements import Activation
    from indra.pipeline import RunnableArgument
    from indra_world.belief import get_eidos_bayesian_scorer
    has_indra_world = True
except ImportError:

@unittest.skipUnless(has_indra_world, 'indra_world not available')
def test_jsonify_arg():
    assert jsonify_arg_input(4) == 4
    assert jsonify_arg_input('test') == 'test'
    assert jsonify_arg_input(True)
    assert not jsonify_arg_input(False)
    assert jsonify_arg_input([1, 2, 3]) == [1, 2, 3]
    assert jsonify_arg_input(location_matches) == {
        'function': 'location_matches', 'no_run': True}
    assert jsonify_arg_input(Activation) == {'stmt_type': 'Activation'}
    assert jsonify_arg_input(RunnableArgument(
        get_eidos_bayesian_scorer,
        {'hume': [13, 7], 'cwms': [13, 7], 'sofia': [13, 7]})) == {
            'function': 'get_eidos_bayesian_scorer',

```
