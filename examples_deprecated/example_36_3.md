# Description
Initialize an empty AssemblyPipeline and append/insert the steps one by one.

# Code
```
from indra.tools.assemble_corpus import filter_no_hypothesis, filter_grounded_only, run_preassembly
from indra_world.ontology import load_world_ontology
from indra_world.belief import get_eidos_scorer
from indra.statements import Agent, Phosphorylation
from .decorators import pipeline_functions, register_pipeline

# Agents and statements for context
map2k1 = Agent('MAP2K1', db_refs={'HGNC': '6840'})
mapk1 = Agent('MAPK1', db_refs={'HGNC': '6871'})
braf = Agent('BRAF')
stmts = [Phosphorylation(map2k1, mapk1, 'T', '185'),

from indra.tools.assemble_corpus import *
from indra_world.ontology import load_world_ontology
from indra_world.belief import get_eidos_scorer
ap = AssemblyPipeline()
ap.append(filter_no_hypothesis)
ap.append(filter_grounded_only)
ap.append(run_preassembly,
          belief_scorer=RunnableArgument(get_eidos_scorer),
          ontology=RunnableArgument(load_world_ontology))
assembled_stmts = ap.run(stmts)

```
