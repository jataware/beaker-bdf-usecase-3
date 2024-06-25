# Description
Retrieve some sample statements while the client continues retrieval in the background.

# Code
```

>> p = get_statements("TNF", timeout=5)
>> some_stmts = p.statements_sample
>>
>> # ...Do some other work...
>>
>> # Wait for the requests to finish before getting the final result.
>> p.wait_until_done()

```
