# Description
Filter evidence related to given papers.

# Code
```

p = get_statements_for_papers([('pmid', '20471474'),
                               ('pmcid', 'PMC3640704')])
all(ev.text_refs['PMID'] == '20471474'
    or ev.text_refs['PMCID'] == 'PMC3640704'
    for s in p.statements for ev in s.evidence)

```
