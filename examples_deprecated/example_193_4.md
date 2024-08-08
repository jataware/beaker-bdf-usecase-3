# Description
Example of processing chemical-disease interactions from files and returning a GnbrProcessor object.

# Code
```
import pandas as pd
import logging
from .processor import GnbrProcessor

base_url = 'https://zenodo.org/record/3459420/files'

def process_chemical_disease(part1_path: str, part2_path: str,
                             indicator_only: bool = True) \
        -> GnbrProcessor:
    """Process chemical–disease interactions.

    Parameters
    ----------
    part1_path :
        Path to the first dataset which contains dependency paths and themes.
    part2_path :
        Path to the second dataset which contains dependency paths and entity
        pairs.
    indicator_only :
        A switch to filter the data which is part of the flagship path set
        for each theme.

    Returns
    -------
    :
        A GnbrProcessor object which contains a list of extracted INDRA
        Statements in its statements attribute.
    """
    return process_from_files(part1_path, part2_path, 'chemical', 'disease',

```
