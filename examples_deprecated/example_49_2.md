# Description
Serialize BioContext object to a JSON serializable dictionary.

# Code
```
class BioContext(Context):
    def __init__(self, location=None, cell_line=None, cell_type=None,
                 organ=None, disease=None, species=None):
        self.location = location
        self.cell_line = cell_line
        self.cell_type = cell_type
        self.organ = organ
        self.disease = disease
        self.species = species


def to_json(self):
    jd = {attr: getattr(self, attr).to_json() for attr in self.attrs
          if getattr(self, attr, None) is not None}
    jd['type'] = 'bio'

```
