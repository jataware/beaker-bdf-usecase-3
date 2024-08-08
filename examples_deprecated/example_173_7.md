# Description
Add hierarchies within Famplex entities.

# Code
```
indra.util import read_unicode_csv
indra.resources import get_resource_path

def add_famplex_hierarchy(self):
    from indra.databases import hgnc_client
    edges = []
    for row in read_unicode_csv(get_resource_path(
            os.path.join('famplex', 'relations.csv')), delimiter=','):
        ns1, id1, rel, ns2, id2 = row
        if ns1 == 'HGNC':
            id1 = hgnc_client.get_current_hgnc_id(id1)
        edges.append((self.label(ns1, id1),
                      self.label(ns2, id2),
                      {'type': rel}))

```
