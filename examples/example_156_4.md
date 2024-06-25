# Description
Method to add a Statement to the network as an edge.

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

def add_edge(self, a1_id, a2_id, stmt):
    """Add a Statement to the network as an edge."""
    stmt_type = stmt.__class__.__name__
    edge_id = self.network.create_edge(a1_id, a2_id, stmt_type)
    evs = []
    for ev in stmt.evidence:
        # We skip evidences with no PMID
        if not ev.pmid:
            continue
        # We take a maximum 200 character snippet of the evidence text
        if not ev.text:
            ev_txt = 'Evidence text not available.'
        elif len(ev.text) > 200:
            ev_txt = ev.text[:200] + '...'
        else:
            ev_txt = ev.text
        # Construct a clickable PMID link with the source and evidence text
        ev_str = ('<a target="_blank" '
                  'href="https://identifiers.org/pubmed:%s">'
                  'pubmed:%s</a> (%s) %s') % (ev.pmid, ev.pmid,
                                              ev.source_api, ev_txt)
        evs.append((ev_str, 0 if ev.text is None else 1))
    # Reorder to have ones with text first
    evs = sorted(evs, key=lambda x: x[1], reverse=True)
    # Cap at 10 pieces of evidence
    evs = [e[0] for e in evs[:10]]
    self.network.set_edge_attribute(edge_id, 'citation', evs,
                                    type='list_of_string')

```
