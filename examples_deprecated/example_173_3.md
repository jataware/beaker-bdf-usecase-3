# Description
Add nodes specific to the HGNC database.

# Code
```

def add_hgnc_nodes(self):
    from indra.databases import hgnc_client
    withdrawns = set(hgnc_client.hgnc_withdrawn)
    nodes = [(self.label('HGNC', hid),
              {'name': hname, 'obsolete': (hid in withdrawns),
               'type': _get_hgnc_type(hgnc_client, hid)})
             for (hid, hname) in hgnc_client.hgnc_names.items()]

```
