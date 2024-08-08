# Description
Load a list or dictionary of INDRA statements from a pickle file.

# Code
```
import pickle
import sys
import logging


def load_statements(fname, as_dict=False):
    """Load statements from a pickle file.

    Parameters
    ----------
    fname : str
        The name of the pickle file to load statements from.
    as_dict : Optional[bool]
        If True and the pickle file contains a dictionary of statements, it
        is returned as a dictionary. If False, the statements are always
        returned in a list. Default: False

    Returns
    -------
    stmts : list
        A list or dict of statements that were loaded.
    """
    logger.info('Loading %s...' % fname)
    with open(fname, 'rb') as fh:
        # Encoding argument not available in pickle for Python 2
        if sys.version_info[0] < 3:
            stmts = pickle.load(fh)
        # Encoding argument specified here to enable compatibility with
        # pickle files created with Python 2
        else:
            stmts = pickle.load(fh, encoding='latin1')

    if isinstance(stmts, dict):
        if as_dict:
            return stmts
        st = []
        for pmid, st_list in stmts.items():
            st += st_list
        stmts = st
    logger.info('Loaded %d statements' % len(stmts))

```
