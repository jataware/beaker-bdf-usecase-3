# Description
Initialize and run an AssemblyPipeline with a list of steps.

# Code
```
from indra.statements import Agent, Phosphorylation
from .decorators import pipeline_functions, register_pipeline

# Agents and statements for context
map2k1 = Agent('MAP2K1', db_refs={'HGNC': '6840'})
mapk1 = Agent('MAPK1', db_refs={'HGNC': '6871'})
braf = Agent('BRAF')
stmts = [Phosphorylation(map2k1, mapk1, 'T', '185'),

steps = [
   {"function": "filter_no_hypothesis"},
   {"function": "filter_grounded_only",
    "kwargs": {"score_threshold": 0.8}}
]
ap = AssemblyPipeline(steps)

```
