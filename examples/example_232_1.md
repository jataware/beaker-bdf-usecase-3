# Description
Construct a list of all phosphorylation sites that have significantly
increased compared to control, and represent these as tuples compatible
with Protmapper (gene_name, 'hgnc', residue, position).

# Code
```
import re
sites = set()
for _, row in df.iterrows():
    if row['feature'] == 'phosphoproteome' and row['logFC'] > 0:
        matches = re.findall(r'([STY]\d+)', row['variableSites'])
        sites |= {(row['gene_name'], 'hgnc', match[0], match[1:]) for match in matches}
sites
```
