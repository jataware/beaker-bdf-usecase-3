# Description
Using `process_pc_pathsbetween` to find paths between a set of genes using PathwayCommons.

# Code
```
import itertools

def process_pc_pathsbetween(gene_names, neighbor_limit=1,
                            database_filter=None, block_size=None):
    """Returns a BiopaxProcessor for a PathwayCommons paths-between query.

    The paths-between query finds the paths between a set of genes. Here
    source gene names are given in a single list and all directions of paths
    between these genes are considered.

    http://www.pathwaycommons.org/pc2/#graph

    http://www.pathwaycommons.org/pc2/#graph_kind

    Parameters
    ----------
    gene_names : list
        A list of HGNC gene symbols to search for paths between.
        Examples: ['BRAF', 'MAP2K1']
    neighbor_limit : Optional[int]
        The number of steps to limit the length of the paths between
        the gene names being queried. Default: 1
    database_filter : Optional[list]
        A list of database identifiers to which the query is restricted.
        Examples: ['reactome'], ['biogrid', 'pid', 'psp']
        If not given, all databases are used in the query. For a full
        list of databases see http://www.pathwaycommons.org/pc2/datasources
    block_size : Optional[int]
        Large paths-between queries (above ~60 genes) can error on the server
        side. In this case, the query can be replaced by a series of
        smaller paths-between and paths-from-to queries each of which contains
        block_size genes.

    Returns
    -------
    bp : BiopaxProcessor
        A BiopaxProcessor containing the obtained BioPAX model in bp.model.
    """
    if not block_size:
        model = model_from_pc_query('pathsbetween',
                                    source=gene_names,
                                    limit=neighbor_limit,
                                    datasource=database_filter)

        if model is not None:
            return process_model(model)
    else:
        gene_blocks = [gene_names[i:i + block_size] for i in
                       range(0, len(gene_names), block_size)]
        stmts = []
        # Run pathsfromto between pairs of blocks and pathsbetween
        # within each block. This breaks up a single call with N genes into
        # (N/block_size)*(N/blocksize) calls with block_size genes
        for genes1, genes2 in itertools.product(gene_blocks, repeat=2):
            if genes1 == genes2:
                bp = process_pc_pathsbetween(genes1,
                                             database_filter=database_filter,
                                             block_size=None)
            else:
                bp = process_pc_pathsfromto(genes1, genes2,
                                            database_filter=database_filter)

```
