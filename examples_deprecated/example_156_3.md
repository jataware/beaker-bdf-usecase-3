# Description
Method to add an Agent to the network as a node.

# Code
```
class NiceCxAssembler(object):
    def __init__(self, stmts=None, network_name=None):
        self.statements = stmts if stmts else []
        self.network = NiceCXNetwork()
        self.network.set_network_attribute('name', (network_name if network_name else 'indra_assembled'))
        self.node_keys = {}
        self.context_prefixes = {'pubmed': 'https://identifiers.org/pubmed:', 'hgnc.symbol': 'https://identifiers.org/hgnc.symbol:'}

    def add_edge(self, a1_id, a2_id, stmt):

    def add_node(self, agent):
        """Add an Agent to the network as a node."""
        agent_key = self.get_agent_key(agent)
        # If the node already exists
        if agent_key in self.node_keys:
            return self.node_keys[agent_key]

        # If the node doesn't exist yet
        db_ns, db_id = agent.get_grounding()
        # TODO: handle more represents name spaces
        if db_ns == 'HGNC':
            represents = 'hgnc.symbol:%s' % agent.name
        else:
            represents = None
        node_id = self.network.create_node(agent.name,
                                           node_represents=represents)
        self.node_keys[agent_key] = node_id

        # Add db_refs as aliases
        db_refs_list = ['%s:%s' % (db_name, db_id)
                        for db_name, db_id in agent.db_refs.items()
                        if db_name in url_prefixes]
        if db_refs_list:
            self.network.add_node_attribute(property_of=node_id,
                                            name='aliases',
                                            values=db_refs_list,
                                            type='list_of_string')

        # Add the type of the node, inferred from grounding
        if db_ns:
            mapped_type = db_ns_type_mappings.get(db_ns)
            if mapped_type:
                self.network.add_node_attribute(property_of=node_id,
                                                name='type',
                                                values=mapped_type,
                                                type='string')


```
