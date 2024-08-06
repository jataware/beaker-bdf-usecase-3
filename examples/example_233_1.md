# Description
Use the protmapper to map the sites to human reference and filter to valid or validly mapped sites

# Code
```
# Use the protmapper to map the sites to human reference
import protmapper
mapped_sites = protmapper.default_mapper.map_sitelist_to_human_ref(sites)

# Filter to valid or validly mapped sites
valid_sites = [ms for ms in mapped_sites if ms.valid or ms.mapped_id]
```
