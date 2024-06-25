# Description
Load extra LINCS data from a local TSV file into a dictionary.

# Code
```

def load_lincs_extras():
    fname = os.path.join(resources, 'hms_lincs_extra.tsv')
    with open(fname, 'r') as fh:
        rows = [line.strip('\n').split('\t') for line in fh.readlines()]
    return {r[0]: {'HMS LINCS ID': r[0],
                   'Name': r[1],
                   'ChEMBL ID': r[2] if r[2] else ''}

```
