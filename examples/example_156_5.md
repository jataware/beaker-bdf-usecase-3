# Description
Method to return the CX string of the assembled model.

# Code
```
class NiceCxAssembler(object):
    def __init__(self, stmts=None, network_name=None):
        self.statements = stmts if stmts else []
        self.network = NiceCXNetwork()
        self.network.set_network_attribute('name', (network_name if network_name else 'indra_assembled'))
        self.node_keys = {}
        self.context_prefixes = {'pubmed': 'https://identifiers.org/pubmed:', 'hgnc.symbol': 'https://identifiers.org/hgnc.symbol:'}

    def add_node(self, agent):
        # Implementation here

    def add_edge(self, a1_id, a2_id, stmt):

def print_model(self):
    """Return the CX string of the assembled model."""

```
