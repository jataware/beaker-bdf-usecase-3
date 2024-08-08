# Description
Running an AssemblyPipeline from a JSON file and manually adding steps, showcasing the general usage of the AssemblyPipeline class.

# Code
```
import os
from indra.pipeline import AssemblyPipeline
from indra.tools.assemble_corpus import filter_no_hypothesis, map_grounding, filter_grounded_only, map_sequence, run_preassembly
stmts = [st1, st2, st3, st4]
path_this = os.path.dirname(os.path.abspath(__file__))

def test_running_pipeline():
    # From json file
    ap = AssemblyPipeline.from_json_file(test_json)
    assert ap
    # AssemblyPipeline has methods for length and iteration
    assert len(ap) == 5
    for step in ap:
        assert step
    assembled_stmts = ap.run(stmts)
    assert assembled_stmts
    assert len(assembled_stmts) == 2
    # By manually adding steps
    ap2 = AssemblyPipeline()
    ap2.append(filter_no_hypothesis)
    ap2.append(map_grounding)
    ap2.append(filter_grounded_only)
    ap2.append(map_sequence)
    ap2.append(run_preassembly, return_toplevel=False)
    assembled_stmts2 = ap2.run(stmts)
    assert assembled_stmts2

```
