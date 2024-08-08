# Description
Use protmapper to map a list of sites (in protmapper format) to human reference and filter to valid or validly mapped sites. The protmapper format is (gene_name, 'hgnc', residue, position)

# Code
```
from protmapper import ProtMapper

# Initialize ProtMapper
pm = ProtMapper()

# Map the sites to human reference and filter
# Sites are in protmapper format (gene_name, 'hgnc', residue, position)
mapped_sites = []
for gene, hgnc, residue, position in sites:
    result = pm.map_to_human_ref(gene, hgnc, residue, position)
    if result.valid:
        mapped_sites.append(result)

# Display the valid or validly mapped sites
print(mapped_sites)
```
