# Description
Plot statement counts for Gene Ontology (GO) terms, distinguishing between statements with genes annotated in GO and those without. This function demonstrates setting up a plot with matplotlib and formatting it appropriately.

# Code
```
import numpy as np
from matplotlib import pyplot as plt

def plot_stmt_counts(go_stmt_map, plot_filename, figsize=(3, 3)):
    # Put together counts for a figure
    pf.set_fig_params()
    fig = plt.figure(figsize=(8, 4), dpi=200)
    ax = fig.gca()
    counts = []
    for go_id in go_stmt_map.keys():
        counts.append((go_stmt_map[go_id]['names'][0],
                       len(go_stmt_map[go_id]['in_go']),
                       len(go_stmt_map[go_id]['not_in_go'])))
    counts.sort(key=lambda x: x[1] + x[2], reverse=True)
    indices = np.arange(len(counts))
    width = 0.8
    in_go = [c[1] for c in counts]
    labels = [c[0] for c in counts]
    not_in_go = [c[2] for c in counts]
    p1 = ax.bar(indices, in_go, width, color='b')
    p2 = ax.bar(indices, not_in_go, width, color='r', bottom=in_go)
    ax.set_ylabel('No. of stmts')
    plt.xlim([-0.2, len(counts)])
    plt.xticks(indices + width/2., labels, rotation='vertical')
    plt.legend((p1[0], p2[0]), ('In GO', 'Not in GO'), frameon=False,
               fontsize=7)
    plt.subplots_adjust(left=0.08, bottom=0.44, top=0.85, right=0.97)
    pf.format_axis(ax)

```
