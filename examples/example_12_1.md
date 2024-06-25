# Description
Return the protein expression levels of genes in specified cell types using the `cbio_client` from the `indra` database.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from copy import copy
from indra.databases import cbio_client
try:
    basestring
except:

def get_protein_expression(gene_names, cell_types):
    """Return the protein expression levels of genes in cell types.

    Parameters
    ----------
    gene_names : list
        HGNC gene symbols for which expression levels are queried.
    cell_types : list
        List of cell type names in which expression levels are queried.
        The cell type names follow the CCLE database conventions.

        Example: LOXIMVI_SKIN, BT20_BREAST

    Returns
    -------
    res : dict[dict[float]]
        A dictionary keyed by cell line, which contains another dictionary
        that is keyed by gene name, with estimated protein amounts as values.
    """
    A = 0.2438361
    B = 3.0957627
    mrna_amounts = cbio_client.get_ccle_mrna(gene_names, cell_types)
    protein_amounts = copy(mrna_amounts)
    for cell_type in cell_types:
        amounts = mrna_amounts.get(cell_type)
        if amounts is None:
            continue
        for gene_name, amount in amounts.items():
            if amount is not None:
                protein_amount = 10**(A * amount + B)
                protein_amounts[cell_type][gene_name] = protein_amount

```
