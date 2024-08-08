# Description
Complex query combining constraints to find specific statements.

# Code
```
from indra.sources.indra_db_rest.api import get_statements_from_query

>> query = (HasAgent("MEK", namespace="FPLX") & HasType(["Inhibition"])
>>          & FromMeshIds(["D001943"]) & HasEvidenceBound(["> 10"]))
>>
>> p = get_statements_from_query(query)

```
