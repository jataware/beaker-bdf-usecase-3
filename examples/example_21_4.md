# Description
How to get an MGI ID from an MGI gene symbol or synonym

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
global mgi_name_to_id, mgi_synonyms_reverse

def get_id_from_name_synonym(name_synonym: str) -> Union[None, str, List[str]]:
    """Return an MGI ID from an MGI gene symbol or synonym.

    If the given name or synonym is the official symbol of a gene, its
    ID is returned. If the input is a synonym, it can correspond to
    one or more genes. If there is a single gene whose synonym matches
    the input, the ID is returned as a string. If multiple genes share
    the given synonym, their IDs are returned in a list. If the input
    doesn't match any names or synonyms, None is returned.

    Parameters
    ----------
    name_synonym :
        The MGI gene symbol or synonym whose ID will be returned.

    Returns
    -------
    :
        The MGI ID (without prefix) of a single gene, a list of MGI IDs,
        or None.
    """
    mgi_id = mgi_name_to_id.get(name_synonym)
    if mgi_id:
        return mgi_id
    mgi_ids = mgi_synonyms_reverse.get(name_synonym)
    if mgi_ids:
        if len(mgi_ids) == 1:
            return mgi_ids[0]
        else:
            return mgi_ids

```
