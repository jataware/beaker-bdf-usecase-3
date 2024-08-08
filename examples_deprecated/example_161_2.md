# Description
Example of how to define and use a weight flattening function

# Code
```

>>> def weight_flattening(G):
...     # Sets the flattened weight to the average of the
...     # inverse source count
...     for edge in G.edges:
...         w = [1/s['evidence_count']
...             for s in G.edges[edge]['statements']]
...         G.edges[edge]['weight'] = sum(w)/len(w)

```
