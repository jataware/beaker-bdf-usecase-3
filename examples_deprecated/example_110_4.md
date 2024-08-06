# Description
Process a CX file with no grounding requirement and ensure names match

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os
indra.sources.ndex_cx import process_cx_file
indra.sources.ndex_cx.processor import NdexCxProcessor

ncp = \
    process_cx_file(os.path.join(path_this, 'merged_BRCA1_formatted.cx'),
                    require_grounding=False)
node_names = list(ncp._node_names.values())
names_from_agents = [ag.name for ag in ncp._node_agents.values()]
texts_from_agents = [ag.db_refs['TEXT'] for ag in ncp._node_agents.values()]
assert set(node_names) == set(names_from_agents)

```
