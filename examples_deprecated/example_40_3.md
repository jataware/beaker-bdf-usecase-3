# Description
Updating UniProt subcellular location information by downloading, parsing the data, and saving the mappings.

# Code
```
os
logging
requests
pandas

def update_uniprot_subcell_loc():
    logger.info('--Updating UniProt subcellular location--')
    url = 'https://www.uniprot.org/docs/subcell.txt'
    res = requests.get(url)
    res.raise_for_status()
    header, entry_block = res.text.split('_' * 75)
    entries = entry_block.split('//')
    mappings = []
    for entry in entries:
        slid = None
        goid = None
        lines = entry.split('\n')
        for line in lines:
            if line.startswith('AC'):
                slid = line[5:].strip()
            if line.startswith('GO'):
                goid = line[5:].split(';')[0]
        if slid and goid:
            mappings.append((slid, goid))
    fname = os.path.join(path, 'uniprot_subcell_loc.tsv')

```
