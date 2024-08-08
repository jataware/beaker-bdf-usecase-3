# Description
Print statistics of the number of sites and the number with any known annotations and explore specific examples of site annotations.

# Code
```
# Print statistics of the number of sites and the number with
# any known annotations
len(stmts_by_site), len([k for k, v in stmts_by_site.items() if v])

# Explore specific examples of site annotations
[s for s in stmts_by_site.items() if s[0][0] == 'EXO1']
```
