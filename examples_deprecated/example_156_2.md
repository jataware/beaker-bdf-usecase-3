# Description
Method to run assembly and return a Nice CX network object.

# Code
```
import json

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

    def make_model(self, self_loops=False, network_attributes=None):
        """Return a Nice CX network object after running assembly.

        Parameters
        ----------
        self_loops : Optional[bool]
            If False, self-loops are excluded from the network. Default: False
        network_attributes : Optional[dict]
            A dictionary containing attributes to be added to the
            assembled network.

        Returns
        -------
        ndex2.nice_cx_network.NiceCXNetwork
            The assembled Nice CX network.
        """
        for stmt in self.statements:
            agents = stmt.agent_list()
            not_none_agents = [a for a in agents if a is not None]
            if len(not_none_agents) < 2:
                continue
            for a1, a2 in itertools.combinations(not_none_agents, 2):
                a1_id = self.add_node(a1)
                a2_id = self.add_node(a2)
                if not self_loops and a1_id == a2_id:
                    continue
                edge_id = self.add_edge(a1_id, a2_id, stmt)

        self.network.set_network_attribute('@context',
                                           json.dumps(self.context_prefixes))
        if network_attributes:
            for k, v in network_attributes.items():
                self.network.set_network_attribute(k, v, 'string')

```
