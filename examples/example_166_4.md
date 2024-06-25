# Description
Generate a networkx graph representing the Kappa contact map (CM) for a given PySB model.

# Code
```
import networkx
from pysb.export import export
from .kappa_util import cm_json_to_networkx

def export_cm_network(model):
    """Return a networkx graph of the model's Kappa contact map.

    Parameters
    ----------
    model : pysb.Model
        A PySB model whose Kappa contact graph is to be generated.

    Returns
    -------
    networkx.Graph
        An undirected networkx graph representing the contact map.
    """
    from .kappa_util import cm_json_to_networkx
    kappa = _prepare_kappa(model)
    cmap = kappa.analyses_contact_map()
    g = cm_json_to_networkx(cmap)

```
