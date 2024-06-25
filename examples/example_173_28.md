# Description
Add nodes and edges for LSPCI entities.

# Code
```
from indra.util import read_unicode_csv

def add_lspci(self):
    lspci = read_unicode_csv(get_resource_path('lspci.tsv'),
                             delimiter='\t')
    nodes_to_add = []
    edges_to_add = []
    next(lspci)
    for (lspcid, name, members_str) in lspci:
        label = self.label('LSPCI', lspcid)
        nodes_to_add.append((label, {'name': name,
                                     'type': 'small_molecule'}))
        members = [member.split(':', maxsplit=1)
                   for member in members_str.split('|')]
        edges_to_add += [(self.label(*member), label, {'type': 'isa'})
                         for member in members]
    self.add_nodes_from(nodes_to_add)

```
