# Description
Render the attributes of a list of Statements as directed graphs.

# Code
```
import logging
from indra.statements.statements import Statement


def draw_stmt_graph(stmts):
    """Render the attributes of a list of Statements as directed graphs.

    The layout works well for a single Statement or a few Statements at a time.
    This function displays the plot of the graph using plt.show().

    Parameters
    ----------
    stmts : list[indra.statements.Statement]
        A list of one or more INDRA Statements whose attribute graph should
        be drawn.
    """
    import networkx
    try:
        import matplotlib.pyplot as plt
    except Exception:
        logger.error('Could not import matplotlib, not drawing graph.')
        return
    try:  # This checks whether networkx has this package to work with.
        import pygraphviz
    except Exception:
        logger.error('Could not import pygraphviz, not drawing graph.')
        return
    import numpy
    g = networkx.compose_all([stmt.to_graph() for stmt in stmts])
    plt.figure()
    plt.ion()
    g.graph['graph'] = {'rankdir': 'LR'}
    pos = networkx.drawing.nx_agraph.graphviz_layout(g, prog='dot')
    g = g.to_undirected()

    # Draw nodes
    options = {
        'marker': 'o',
        's': 200,
        'c': [0.85, 0.85, 1],
        'facecolor': '0.5',
        'lw': 0,
    }
    ax = plt.gca()
    nodelist = list(g)
    xy = numpy.asarray([pos[v] for v in nodelist])
    node_collection = ax.scatter(xy[:, 0], xy[:, 1], **options)
    node_collection.set_zorder(2)
    # Draw edges
    networkx.draw_networkx_edges(g, pos, arrows=False, edge_color='0.5')
    # Draw labels
    edge_labels = {(e[0], e[1]): e[2].get('label') for e in g.edges(data=True)}
    networkx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
    node_labels = {n[0]: n[1].get('label') for n in g.nodes(data=True)}
    for key, label in node_labels.items():
        if len(label) > 25:
            parts = label.split(' ')
            parts.insert(int(len(parts)/2), '\n')
            label = ' '.join(parts)
            node_labels[key] = label
    networkx.draw_networkx_labels(g, pos, labels=node_labels)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

```
