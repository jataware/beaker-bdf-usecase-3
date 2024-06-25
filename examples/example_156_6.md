# Description
Method to add INDRA Statements to the assembler's list of statements.

# Code
```
class CxAssembler(object):
    def __init__(self, stmts=None, network_name=None):
        if stmts is None:
            self.statements = []
        else:
            self.statements = stmts
        if network_name is None:
            self.network_name = 'indra_assembled'
        else:
            self.network_name = network_name
        self.cx = {'nodes': [], 'edges': [], 'nodeAttributes': [], 'edgeAttributes': [], 'citations': [], 'edgeCitations': [], 'supports': [], 'edgeSupports': [], 'networkAttributes': []}
        self._existing_nodes = {}
        self._existing_edges = {}

    def add_statements(self, stmts):
        """Add INDRA Statements to the assembler's list of statements.

        Parameters
        ----------
        stmts : list[indra.statements.Statement]
            A list of :py:class:`indra.statements.Statement`
            to be added to the statement list of the assembler.
        """
        for stmt in stmts:

```
