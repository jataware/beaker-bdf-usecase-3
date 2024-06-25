# Description
Add cross-references (xrefs) between HGNC, UniProt, and Entrez Gene IDs.

# Code
```
from indra.databases import hgnc_client

    def add_hgnc_uniprot_entrez_xrefs(self):
        from indra.databases import hgnc_client
        from indra.databases import uniprot_client
        edges = []
        for hid, upid in hgnc_client.uniprot_ids.items():
            uids = upid.split(', ')
            preferred = hgnc_client.uniprot_ids_preferred.get(hid)
            if preferred:
                uids = [preferred]
            for uid in uids:
                edge_data = {'type': 'xref', 'source': 'hgnc'}
                edges.append((self.label('HGNC', hid), self.label('UP', uid),
                              edge_data))
        self.add_edges_from(edges)

        edges = [(self.label('UP', uid), self.label('HGNC', hid),
                  {'type': 'xref', 'source': 'hgnc'})
                 for uid, hid in uniprot_client.um.uniprot_hgnc.items()]
        self.add_edges_from(edges)

        edges = [(self.label('UP', uid), self.label('EGID', egid),
                  {'type': 'xref', 'source': 'uniprot'})
                 for uid, egid in uniprot_client.um.uniprot_entrez.items()]
        edges += [(self.label('EGID', egid), self.label('UP', uid),
                  {'type': 'xref', 'source': 'uniprot'})
                  for egid, uid in uniprot_client.um.entrez_uniprot.items()]

```
