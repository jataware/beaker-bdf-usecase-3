# Description
Dump a list of INDRA statements into a pickle file.

# Code
```
import pickle
import logging
from indra.pipeline import register_pipeline


@register_pipeline
def dump_statements(stmts_in, fname, protocol=4):
    """Dump a list of statements into a pickle file.

    Parameters
    ----------
    fname : str
        The name of the pickle file to dump statements into.
    protocol : Optional[int]
        The pickle protocol to use (use 2 for Python 2 compatibility).
        Default: 4
    """
    logger.info('Dumping %d statements into %s...' % (len(stmts_in), fname))
    with open(fname, 'wb') as fh:
        pickle.dump(stmts_in, fh, protocol=protocol)

```
