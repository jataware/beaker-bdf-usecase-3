# Description
Get statements that have database evidence and have either MEK or MAP2K1 as a name for any of its agents.

# Code
```
from indra.sources.indra_db_rest.api import get_statements_from_query

>>>
>> from indra.sources.indra_db_rest.api import get_statements_from_query
>> from indra.sources.indra_db_rest.query import *
>> q = HasAgent('MEK') | HasAgent('MAP2K1') & HasDatabases()
>> p = get_statements_from_query(q)
>> p.statements
[Activation(MEK(), ERK()),
 Phosphorylation(MEK(), ERK()),
 Activation(MAP2K1(), ERK()),
 Activation(RAF1(), MEK()),
 Phosphorylation(RAF1(), MEK()),
 Phosphorylation(MAP2K1(), ERK()),
 Activation(BRAF(), MEK()),
 Inhibition(2-(2-amino-3-methoxyphenyl)chromen-4-one(), MEK()),
 Activation(MAP2K1(), MAPK1()),
 Activation(MAP2K1(), MAPK3()),
 Phosphorylation(MAP2K1(), MAPK1()),
 Phosphorylation(BRAF(), MEK()),
 Activation(MEK(), MAPK1()),
 Complex(BRAF(), MAP2K1()),
 Phosphorylation(MAP2K1(), MAPK3()),
 Activation(MEK(), MAPK3()),
 Complex(MAP2K1(), RAF1()),
 Activation(RAF1(), MAP2K1()),
 Inhibition(trametinib(), MEK()),
 Phosphorylation(MEK(), MAPK3()),
 Complex(MAP2K1(), MAPK1()),
 Phosphorylation(MEK(), MAPK1()),
 Inhibition(selumetinib(), MEK()),

```
