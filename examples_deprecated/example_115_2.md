# Description
Demonstrating various methods of the AssemblyPipeline class, including inserting steps, appending functions with arguments, and using RunnableArgument.

# Code
```
from indra.pipeline import AssemblyPipeline, RunnableArgument
from indra.tools.assemble_corpus import filter_no_hypothesis, filter_grounded_only, filter_by_type, run_preassembly
from indra.statements import Activation
try:
    from indra_world.assembly.matches import location_matches
    from indra_world.assembly.refinement import location_refinement
    from indra_world.belief import get_eidos_scorer
    from indra_world.ontology import world_ontology
    has_indra_world = True
except ImportError:

@unittest.skipUnless(has_indra_world, 'indra_world not available')
def test_pipeline_methods():
    ap = AssemblyPipeline()
    assert len(ap) == 0
    ap.append(filter_grounded_only)
    assert len(ap) == 1
    ap.insert(0, filter_no_hypothesis)
    assert len(ap) == 2
    assert ap.steps[0] == {'function': 'filter_no_hypothesis'}
    # Append functions with arguments and runnable arguments
    ap.append(filter_by_type, Activation)
    assert len(ap) == 3
    assert ap.steps[2] == {'function': 'filter_by_type',
                           'args': [{'stmt_type': 'Activation'}]}, ap.steps[2]
    ap.append(
        run_preassembly, matches_fun=location_matches,
        refinement_fun=location_refinement, normalize_equivalences=True,
        normalize_opposites=True, normalize_ns='WM',
        belief_scoret=RunnableArgument(get_eidos_scorer),
        ontology=world_ontology)
    assert len(ap) == 4
    assert isinstance(ap.steps[3], dict)
    assert isinstance(ap.steps[3]['kwargs'], dict)
    assert len(ap.steps[3]['kwargs']) == 7
    # Run argument to get value
    assert isinstance(ap.get_argument_value({'function': 'get_eidos_scorer'}),
                      BeliefScorer)
    # Get a function object as argument
    assert ap.get_argument_value(
        {'function': 'location_matches', 'no_run': True}) == location_matches
    # Get statement type as argument
    assert ap.get_argument_value({'stmt_type': 'Activation'}) == Activation
    # Get simple argument values
    assert ap.get_argument_value('test') == 'test'
    assert ap.get_argument_value(4) == 4
    assert ap.get_argument_value(True)
    assert not ap.get_argument_value(False)

```
