# Description
Using `process_pc_pathsfromto` to find paths from a set of source genes to a set of target genes using PathwayCommons.

# Code
```
import itertools

def process_pc_pathsfromto(source_genes, target_genes, neighbor_limit=1,
                           database_filter=None):
    """Returns a BiopaxProcessor for a PathwayCommons paths-from-to query.

    The paths-from-to query finds the paths from a set of source genes to
    a set of target genes.

    http://www.pathwaycommons.org/pc2/#graph

    http://www.pathwaycommons.org/pc2/#graph_kind

    Parameters
    ----------
    source_genes : list
        A list of HGNC gene symbols that are the sources of paths being
        searched for.
        Examples: ['BRAF', 'RAF1', 'ARAF']
    target_genes : list
        A list of HGNC gene symbols that are the targets of paths being
        searched for.
        Examples: ['MAP2K1', 'MAP2K2']
    neighbor_limit : Optional[int]
        The number of steps to limit the length of the paths
        between the source genes and target genes being queried. Default: 1
    database_filter : Optional[list]
        A list of database identifiers to which the query is restricted.
        Examples: ['reactome'], ['biogrid', 'pid', 'psp']
        If not given, all databases are used in the query. For a full
        list of databases see http://www.pathwaycommons.org/pc2/datasources

    Returns
    -------
    bp : BiopaxProcessor
        A BiopaxProcessor containing the obtained BioPAX model in bp.model.
    """
    model = model_from_pc_query('pathsfromto',
                                source=source_genes,
                                target=target_genes,
                                limit=neighbor_limit,
                                datasource=database_filter)
    if model is not None:

```
