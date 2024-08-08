# Description
Example of getting relevant statements from Pathway Commons using either 'paths between' or 'neighborhood' queries, potentially filtering them, and caching the results.

# Code
```
import os
import pickle
import logging
from indra.sources import biopax
import indra.tools.assemble_corpus as ac

logger = logging.getLogger(__name__)

class GeneNetwork(object):
    def __init__(self, gene_list, basename=None):
        if not gene_list:
            raise ValueError("Gene list must contain at least one element.")
        self.gene_list = gene_list

    def get_biopax_stmts(self, filter=False, query='pathsbetween',
                         database_filter=None):
        """Get relevant statements from Pathway Commons.

        Performs a "paths between" query for the genes in :py:attr:`gene_list`
        and uses the results to build statements. This function caches two
        files: the list of statements built from the query, which is cached in
        `<basename>_biopax_stmts.pkl`, and the OWL file returned by the Pathway
        Commons Web API, which is cached in `<basename>_pc_pathsbetween.owl`.
        If these cached files are found, then the results are returned based
        on the cached file and Pathway Commons is not queried again.

        Parameters
        ----------
        filter : Optional[bool]
            If True, includes only those statements that exclusively mention
            genes in :py:attr:`gene_list`. Default is False.
        query : Optional[str]
            Defined what type of query is executed. The two options are
            'pathsbetween' which finds paths between the given list of genes
            and only works if more than 1 gene is given, and 'neighborhood'
            which searches the immediate neighborhood of each given gene.
            Note that for pathsbetween queries with more thatn 60 genes, the
            query will be executed in multiple blocks for scalability.
        database_filter: Optional[list[str]]
            A list of PathwayCommons databases to include in the query.

        Returns
        -------
        list of :py:class:`indra.statements.Statement`
            List of INDRA statements extracted from Pathway Commons.
        """
        # If we're using a cache, initialize the appropriate filenames
        if self.basename is not None:
            biopax_stmt_path = '%s_biopax_stmts.pkl' % self.basename
            biopax_ras_owl_path = '%s_pc_pathsbetween.owl' % self.basename
        # Check for cached Biopax stmt file at the given path
        # if it's there, return the statements from the cache
        if self.basename is not None and os.path.exists(biopax_stmt_path):
            logger.info("Loading Biopax statements from %s" % biopax_stmt_path)
            with open(biopax_stmt_path, 'rb') as f:
                bp_statements = pickle.load(f)
            return bp_statements
        # Check for cached file before querying Pathway Commons Web API
        if self.basename is not None and os.path.exists(biopax_ras_owl_path):
            logger.info("Loading Biopax from OWL file %s" % biopax_ras_owl_path)
            bp = biopax.process_owl(biopax_ras_owl_path)
        # OWL file not found; do query and save to file
        else:
            if (len(self.gene_list) < 2) and (query == 'pathsbetween'):
                logger.warning('Using neighborhood query for one gene.')
                query = 'neighborhood'
            if query == 'pathsbetween':
                if len(self.gene_list) > 60:
                    block_size = 60
                else:
                    block_size = None
                bp = biopax.process_pc_pathsbetween(self.gene_list,
                                                database_filter=database_filter,
                                                block_size=block_size)
            elif query == 'neighborhood':
                bp = biopax.process_pc_neighborhood(self.gene_list,
                                                database_filter=database_filter)
            else:
                logger.error('Invalid query type: %s' % query)
                return []
            # Save the file if we're caching
            if self.basename is not None:
                bp.save_model(biopax_ras_owl_path)
        # Save statements to pickle file if we're caching
        if self.basename is not None:
            with open(biopax_stmt_path, 'wb') as f:
                pickle.dump(bp.statements, f)
        # Optionally filter out statements not involving only our gene set
        if filter:
            policy = 'one' if len(self.gene_list) > 1 else 'all'
            stmts = ac.filter_gene_list(bp.statements, self.gene_list, policy)
        else:
            stmts = bp.statements

```
