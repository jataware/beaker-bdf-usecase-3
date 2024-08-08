# Description
Add nodes specific to the UniProt database.

# Code
```

    def add_uniprot_nodes(self):
        from indra.databases import uniprot_client

        nodes = [(self.label('UP', uid),
                  {'name': uname,
                   'type': _get_uniprot_type(uniprot_client, uid)})
                 for (uid, uname)
                 in uniprot_client.um.uniprot_gene_name.items()]
        for sec_id in uniprot_client.um.uniprot_sec:
            nodes.append((self.label('UP', sec_id), {'obsolete': True}))

```
