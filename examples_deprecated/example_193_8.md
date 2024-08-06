# Description
Example of processing chemical-disease interactions from the web and returning a GnbrProcessor object.

# Code
```
import pandas as pd
import logging
from .processor import GnbrProcessor

base_url = 'https://zenodo.org/record/3459420/files'

def process_chemical_disease_from_web(indicator_only: bool = True)\
        -> GnbrProcessor:
    """Call process_chemical_disease function on the GNBR datasets.

    Parameters
    ----------
    indicator_only :
        A switch to filter the data which is part of the flagship path set
        for each theme.

    Returns
    -------
    :
        A GnbrProcessor object which contains a list of extracted INDRA
        Statements in its statements attribute.
    """
    return process_from_web('chemical', 'disease',

```
