# Description
Process ACSN data directly from the web.

# Code
```
from typing import Mapping
import pandas
import requests
from .processor import AcsnProcessor

ACSN_URL = 'https://acsn.curie.fr/ACSN2/downloads/'
ACSN_RELATIONS_URL = ACSN_URL + 'ACSN2_binary_relations_between_proteins_with_PMID.txt'
ACSN_CORRESPONDENCE_URL = ACSN_URL + 'ACSN2_HUGO_Correspondence.gmt'


def _transform_gmt(gmt):
    """Convert ACSN correspondence GMT file into a dictionary."""
    acsn_hgnc_dict = {}
    for line in gmt:
        parts = line.strip().split('\t')
        acsn_hgnc_dict[parts[0]] = parts[2:]
    return acsn_hgnc_dict

def process_df(relations_df: pandas.DataFrame, correspondence_dict: Mapping) -> AcsnProcessor:
    """Process ACSN data from input data structures."""
    ap = AcsnProcessor(relations_df, correspondence_dict)
    ap.extract_statements()

def process_from_web() -> AcsnProcessor:
    """Process ACSN data directly from the web.

    Returns
    -------
    :
        A processor with a list of INDRA statements that were extracted
        in its statements attribute.
    """
    relations_df = pandas.read_csv(ACSN_RELATIONS_URL, sep='\t')
    correspondence_dict = _transform_gmt(
        requests.get(ACSN_CORRESPONDENCE_URL).text.split('\n'))

```
