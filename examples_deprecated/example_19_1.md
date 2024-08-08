# Description
Load the LINCS drug target data into a list of dictionaries by fetching and processing a CSV file from a URL.

# Code
```
import os
import sys
import requests
from io import StringIO, BytesIO
from indra.util import read_unicode_csv_fileobj


def get_drug_target_data():
    """Load the csv into a list of dicts containing the LINCS drug target data.

    Returns
    -------
    data : list[dict]
        A list of dicts, each keyed based on the header of the csv, with values
        as the corresponding column values.
    """
    url = LINCS_URL + '/datasets/20000/results'

```
