# Description
Load a file with serialized statement results and return the loaded results. It provides a simple utility function to read and deserialize data from a file using the pickle module.

# Code
```
import logging
import pickle


def load_file(stmts_file):
    logger.info("Loading results...")
    with open(stmts_file, 'rb') as f:
        results = pickle.load(f)

```
