# Description
Example of how to define and use a belief flattening function

# Code
```

>>> def belief_flattening(G, edge):
...     # Return the average belief score of the constituent edges
...     all_beliefs = [s['belief']
...         for s in G.edges[edge]['statements']]

```
