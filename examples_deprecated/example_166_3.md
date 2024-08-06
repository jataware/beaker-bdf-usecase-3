# Description
Export a PySB model into a Kappa contact map (CM) represented as a networkx graph. Optionally, render the CM into a file with the specified format.

# Code
```
import networkx
from pysb.export import export
from .kappa_util import cm_json_to_graph

def export_kappa_cm(model, fname=None):
    """Return a networkx graph representing the model's Kappa contact map.

    Parameters
    ----------
    model : pysb.core.Model
        A PySB model to be exported into a Kappa CM.
    fname : Optional[str]
        A file name, typically with .png or .pdf extension in which
        the CM is rendered using pygraphviz.

    Returns
    -------
    npygraphviz.Agraph
        A graph object representing the contact map.
    """
    from .kappa_util import cm_json_to_graph
    kappa = _prepare_kappa(model)
    cmap = kappa.analyses_contact_map()
    cm = cm_json_to_graph(cmap)
    if fname:
        cm.draw(fname, prog='dot')

```
