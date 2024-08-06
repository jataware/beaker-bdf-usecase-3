# Description
How to get the MGI gene symbol for a given MGI ID

# Code
```
from collections import defaultdict
from typing import List, Union
from indra.util import read_unicode_csv
from indra.resources import get_resource_path

# Initialize data structures using the _read_mgi function
def _read_mgi():
    fname = get_resource_path('mgi_entries.tsv')
    mgi_id_to_name = {}
    mgi_name_to_id = {}
    mgi_synonyms = {}
    mgi_synonyms_reverse = defaultdict(list)
    mgi_id_to_ensembl = {}
    for mgi_id, name, synonyms_str, ensembl_id in read_unicode_csv(fname, '\t'):
        if name:
            mgi_id_to_name[mgi_id] = name
            mgi_name_to_id[name] = mgi_id
        if synonyms_str:
            synonyms = synonyms_str.split('|')
            mgi_synonyms[mgi_id] = synonyms
            for synonym in synonyms:
                mgi_synonyms_reverse[synonym].append(mgi_id)
        if ensembl_id:
            mgi_id_to_ensembl[mgi_id] = ensembl_id

    return mgi_id_to_name, mgi_name_to_id, mgi_synonyms, dict(mgi_synonyms_reverse), mgi_id_to_ensembl

# Read and assign data structures
global mgi_id_to_name

def get_name_from_id(mgi_id: str) -> Union[str, None]:
    """Return the MGI gene symbol for a given MGI ID.

    Parameters
    ----------
    mgi_id :
        The MGI ID (without prefix) whose symbol will be returned.

    Returns
    -------
    :
        The MGI symbol for the given ID or None if not available.
    """
    if mgi_id and mgi_id.startswith('MGI:'):
        mgi_id = mgi_id[4:]

```
