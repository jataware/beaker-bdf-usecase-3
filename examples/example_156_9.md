# Description
Method to save the assembled CX network in a file.

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

    def save_model(self, file_name='model.cx'):
        """Save the assembled CX network in a file.

        Parameters
        ----------
        file_name : Optional[str]
            The name of the file to save the CX network to. Default: model.cx
        """
        with open(file_name, 'wt') as fh:
            cx_str = self.print_cx()

```
