# Description
Example of getting relevant statements from the BEL large corpus, potentially filtering them, and caching the results.

# Code
```
import pickle
from indra.sources import bel
import indra.tools.assemble_corpus as ac

class GeneNetwork(object):
    def __init__(self, gene_list, basename=None):
        if not gene_list:
            raise ValueError("Gene list must contain at least one element.")
        self.gene_list = gene_list

    def get_bel_stmts(self, filter=False):
        """Get relevant statements from the BEL large corpus.

        Performs a series of neighborhood queries and then takes the union of
        all the statements. Because the query process can take a long time for
        large gene lists, the resulting list of statements are cached in a
        pickle file with the filename `<basename>_bel_stmts.pkl`.  If the
        pickle file is present, it is used by default; if not present, the
        queries are performed and the results are cached.

        Parameters
        ----------
        filter : bool
            If True, includes only those statements that exclusively mention
            genes in :py:attr:`gene_list`. Default is False. Note that the
            full (unfiltered) set of statements are cached.

        Returns
        -------
        list of :py:class:`indra.statements.Statement`
            List of INDRA statements extracted from the BEL large corpus.
        """
        bel_proc = bel.process_pybel_neighborhood(self.gene_list)
        bel_statements = bel_proc.statements
        # Save to pickle file if we're caching
        if self.basename is not None:
            with open('%s_bel_stmts.pkl' % self.basename, 'wb') as f:
                pickle.dump(bel_statements, f)
        # Optionally filter out statements not involving only our gene set
        if filter:
            if len(self.gene_list) > 1:
                bel_statements = ac.filter_gene_list(bel_statements,
                                                     self.gene_list, 'all')

```
