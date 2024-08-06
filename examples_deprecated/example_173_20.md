# Description
Add replacements for UniProt IDs.

# Code
```

def add_uniprot_replacements(self):
    from indra.databases import uniprot_client
    edges = []
    for sec_id, prim_ids in uniprot_client.um.uniprot_sec.items():
        if len(prim_ids) == 1:
            edges.append((self.label('UP', sec_id),
                          self.label('UP', prim_ids[0]),
                          {'type': 'replaced_by'}))

```
