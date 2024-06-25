# Description
Filter evidence related to given papers without evidence filtering.

# Code
```

p = get_statements_for_papers([('pmid', '20471474'),
                               ('pmcid', 'PMC3640704')], filter_ev=False)
all(ev.text_refs['PMID'] == '20471474'
    or ev.text_refs['PMCID'] == 'PMC3640704'
    for s in p.statements for ev in s.evidence)

```
