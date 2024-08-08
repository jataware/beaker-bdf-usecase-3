# Description
Example of processing gene-gene interactions from the web and returning a GnbrProcessor object.

# Code
```
import pandas as pd
import logging
from .processor import GnbrProcessor

base_url = 'https://zenodo.org/record/3459420/files'

def process_gene_gene_from_web(indicator_only: bool = True) -> GnbrProcessor:
    """Call process_gene_gene function on the GNBR datasets.

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

```
