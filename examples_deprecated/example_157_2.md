# Description
Main program execution for adding a semantic hub layout to a CX network from a file and specifying the hub node.

# Code
```
import json

def add_semantic_hub_layout(cx, hub: str):
    graph = cx_to_networkx(cx)
    hub_node = get_node_by_name(graph, hub)
    node_classes = classify_nodes(graph, hub_node)
    layout_aspect = get_layout_aspect(hub_node, node_classes)

if __name__ == '__main__':
    with open('CDK13.cx', 'r') as fh:
        cx = json.load(fh)

```
