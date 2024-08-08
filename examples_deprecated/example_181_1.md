# Description
Using `process_pc_neighborhood` to query the neighborhood around a set of source genes using PathwayCommons.

# Code
```
import itertools

def process_pc_neighborhood(gene_names, neighbor_limit=1,
                            database_filter=None):
    """Returns a BiopaxProcessor for a PathwayCommons neighborhood query.

    The neighborhood query finds the neighborhood around a set of source genes.

    http://www.pathwaycommons.org/pc2/#graph

    http://www.pathwaycommons.org/pc2/#graph_kind

    Parameters
    ----------
    gene_names : list
        A list of HGNC gene symbols to search the neighborhood of.
        Examples: ['BRAF'], ['BRAF', 'MAP2K1']
    neighbor_limit : Optional[int]
        The number of steps to limit the size of the neighborhood around
        the gene names being queried. Default: 1
    database_filter : Optional[list]
        A list of database identifiers to which the query is restricted.
        Examples: ['reactome'], ['biogrid', 'pid', 'psp']
        If not given, all databases are used in the query. For a full
        list of databases see http://www.pathwaycommons.org/pc2/datasources

    Returns
    -------
    BiopaxProcessor
        A BiopaxProcessor containing the obtained BioPAX model in its model
        attribute and a list of extracted INDRA Statements from the model in
        its statements attribute.
    """
    model = model_from_pc_query('neighborhood', source=gene_names,
                                limit=neighbor_limit,
                                datasource=database_filter)
    if model is not None:

```
