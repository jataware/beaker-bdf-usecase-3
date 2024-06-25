# Description
An example of using the `~` operator to negate a query.

# Code
```
from indra.sources.indra_db_rest.api import get_statements_from_query

>> q = HasAgent('MEK', namespace='FPLX') & ~HasAgent('ERK', namespace='FPLX')
>> p = get_statements_from_query(q)
>> p.statements[:10]
[Phosphorylation(None, MEK()),
 Phosphorylation(RAF(), MEK()),
 Activation(RAF(), MEK()),
 Activation(MEK(), MAPK()),
 Inhibition(U0126(), MEK()),
 Inhibition(MEK(), apoptotic process()),
 Activation(MEK(), cell population proliferation()),
 Activation(RAF1(), MEK()),
 Phosphorylation(MEK(), MAPK()),

```
