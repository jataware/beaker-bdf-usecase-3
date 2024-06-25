# Description
Export a PySB model into a Kappa influence map (IM) represented as a networkx MultiDiGraph. Optionally, render the IM into a file with the specified format.

# Code
```
import networkx
from pysb.export import export
from .kappa_util import im_json_to_graph

def export_kappa_im(model, fname=None):
    """Return a networkx graph representing the model's Kappa influence map.

    Parameters
    ----------
    model : pysb.core.Model
        A PySB model to be exported into a Kappa IM.
    fname : Optional[str]
        A file name, typically with .png or .pdf extension in which
        the IM is rendered using pygraphviz.

    Returns
    -------
    networkx.MultiDiGraph
        A graph object representing the influence map.
    """
    from .kappa_util import im_json_to_graph
    kappa = _prepare_kappa(model)
    imap = kappa.analyses_influence_map()
    im = im_json_to_graph(imap)
    for param in model.parameters:
        try:
            im.remove_node(param.name)
        except:
            pass
    if fname:
        agraph = networkx.nx_agraph.to_agraph(im)
        agraph.draw(fname, prog='dot')

```
