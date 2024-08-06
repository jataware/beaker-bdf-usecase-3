# Description
Get statements that have an agent MEK and an agent ERK and more than 10 evidence.

# Code
```
from indra.sources.indra_db_rest.api import get_statements_from_query

>>>
>> q = HasAgent('MEK') & HasAgent('ERK') & HasEvidenceBound(["> 10"])
>> p = get_statements_from_query(q)
>> p.statements
[Activation(MEK(), ERK()),
 Phosphorylation(MEK(), ERK()),
 Complex(ERK(), MEK()),
 Inhibition(MEK(), ERK()),
 Dephosphorylation(MEK(), ERK()),
 Complex(ERK(), MEK(), RAF()),
 Phosphorylation(MEK(), ERK(), T),
 Phosphorylation(MEK(), ERK(), Y),
 Activation(MEK(), ERK(mods: (phosphorylation))),

```
