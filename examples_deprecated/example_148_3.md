# Description
Example of running a complete preassembly procedure on a given list of statements, printing a summary, and caching the results.

# Code
```
import pickle
import indra.tools.assemble_corpus as ac

class GeneNetwork(object):
    def __init__(self, gene_list, basename=None):
        if not gene_list:
            raise ValueError("Gene list must contain at least one element.")
        self.gene_list = gene_list

    def run_preassembly(self, stmts, print_summary=True):
        """Run complete preassembly procedure on the given statements.

        Results are returned as a dict and stored in the attribute
        :py:attr:`results`. They are also saved in the pickle file
        `<basename>_results.pkl`.

        Parameters
        ----------
        stmts : list of :py:class:`indra.statements.Statement`
            Statements to preassemble.
        print_summary : bool
            If True (default), prints a summary of the preassembly process to
            the console.

        Returns
        -------
        dict
            A dict containing the following entries:

            - `raw`: the starting set of statements before preassembly.
            - `duplicates1`: statements after initial de-duplication.
            - `valid`: statements found to have valid modification sites.
            - `mapped`: mapped statements (list of
              :py:class:`indra.preassembler.sitemapper.MappedStatement`).
            - `mapped_stmts`: combined list of valid statements and statements
              after mapping.
            - `duplicates2`: statements resulting from de-duplication of the
              statements in `mapped_stmts`.
            - `related2`: top-level statements after combining the statements
              in `duplicates2`.
        """
        stmts = ac.map_grounding(stmts)
        stmts = ac.map_sequence(stmts)
        self.results = ac.run_preassembly(stmts)
        # Save the results if we're caching
        if self.basename is not None:
            results_filename = '%s_results.pkl' % self.basename
            with open(results_filename, 'wb') as f:
                pickle.dump(self.results, f)

```
