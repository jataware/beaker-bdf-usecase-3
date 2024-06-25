# Description
Add nodes for Famplex entities.

# Code
```
indra.util import read_unicode_csv
indra.resources import get_resource_path

def add_famplex_nodes(self):
    nodes = []
    for row in read_unicode_csv(get_resource_path(
            os.path.join('famplex', 'entities.csv')), delimiter=','):
        entity = row[0]
        nodes.append((self.label('FPLX', entity),
                      {'name': entity,
                       'type': 'protein_family_complex'}))

```
