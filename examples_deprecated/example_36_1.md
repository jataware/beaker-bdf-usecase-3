# Description
Initialize and run an AssemblyPipeline from a JSON file containing the steps.

# Code
```
import os
from indra.statements import Agent, Phosphorylation
from .decorators import pipeline_functions, register_pipeline

# Agents and statements for context
map2k1 = Agent('MAP2K1', db_refs={'HGNC': '6840'})
mapk1 = Agent('MAPK1', db_refs={'HGNC': '6871'})
braf = Agent('BRAF')
stmts = [Phosphorylation(map2k1, mapk1, 'T', '185'),

import os
path_this = os.path.dirname(os.path.abspath(__file__))
filename = os.path.abspath(
os.path.join(path_this, '..', 'tests', 'pipeline_test.json'))
ap = AssemblyPipeline.from_json_file(filename)

```
