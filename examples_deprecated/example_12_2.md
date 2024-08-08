# Description
Return protein amino acid changes in given genes and cell types using the `cbio_client` from the `indra` database.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.databases import cbio_client
try:
    basestring
except:

def get_mutations(gene_names, cell_types):
    """Return protein amino acid changes in given genes and cell types.

    Parameters
    ----------
    gene_names : list
        HGNC gene symbols for which mutations are queried.
    cell_types : list
        List of cell type names in which mutations are queried.
        The cell type names follow the CCLE database conventions.

        Example: LOXIMVI_SKIN, BT20_BREAST

    Returns
    -------
    res : dict[dict[list]]
        A dictionary keyed by cell line, which contains another dictionary
        that is keyed by gene name, with a list of amino acid substitutions
        as values.
    """
    mutations = cbio_client.get_ccle_mutations(gene_names, cell_types)

```
