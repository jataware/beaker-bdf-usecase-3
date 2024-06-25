# Description
Form unions in query constraints to find statements.

# Code
```
from indra.sources.indra_db_rest.api import get_statements_from_query

>> query = (
>>     (
>>         HasAgent("MEK", namespace="FPLX")
>>         | HasAgent("MAP2K1", namespace="HGNC-SYMBOL")
>>     )
>>     & HasType(['Inhibition'])
>> )
>>

```
