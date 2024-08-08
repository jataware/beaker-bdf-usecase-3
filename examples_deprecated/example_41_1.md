# Description
Automatically load the latest DrugBank data and save the processed statements to a file using pickle.

# Code
```

import pickle
import indra.sources.drugbank
processor = indra.sources.drugbank.get_drugbank_processor()
with open('drugbank_indra_statements.pkl', 'wb') as file:

```
