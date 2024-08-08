# Description
Process TAS data from a local CSV file and return a TasProcessor object with the specified options.

# Code
```
import csv
import logging
import requests
from hashlib import md5
from .processor import TasProcessor
from indra.util import read_unicode_csv

tas_data_url = 'https://bigmech.s3.amazonaws.com/indra-db/tas.csv'
tas_resource_md5 = '554ccba4617aae7b3b06a62893424c7f'
logger = logging.getLogger(__name__)

def _load_data(data_iter):
    headers = data_iter[0]
    data = [{header: val for header, val in zip(headers, line)} for line in data_iter[1:]]

def process_csv(fname, affinity_class_limit=2, named_only=False,
                standardized_only=False):
    """Return a TasProcessor for the contents of a given CSV file..

    Interactions are classified into the following classes based on affinity:
      | 1  -- Kd < 100nM
      | 2  -- 100nM < Kd < 1uM
      | 3  -- 1uM < Kd < 10uM
      | 10 -- Kd > 10uM
    By default, only classes 1 and 2 are extracted but the affinity_class_limit
    parameter can be used to change the upper limit of extracted classes.

    Parameters
    ----------
    fname : str
        The path to a local CSV file containing the TAS data.
    affinity_class_limit : Optional[int]
        Defines the highest class of binding affinity that is included in the
        extractions. Default: 2
    named_only : Optional[bool]
        If True, only chemicals that have a name assigned in some name space
        (including ones that aren't fully stanadardized per INDRA's ontology,
        e.g., CHEMBL1234) are included. If False, chemicals whose name is
        assigned based on an ID (e.g., CHEMBL)rather than an actual name are
        also included. Default: False
    standardized_only : Optional[bool]
        If True, only chemicals that are fully standardized per INDRA's
        ontology (i.e., they have grounding appearing in one of the
        default_ns_order name spaces, and consequently have any
        groundings and their name standardized) are extracted.
        Default: False

    Returns
    -------
    TasProcessor
        A TasProcessor object which has a list of INDRA Statements extracted
        from the CSV file representing drug-target inhibitions in its
        statements attribute.
    """
    data_iter = list(read_unicode_csv(fname))
    return TasProcessor(_load_data(data_iter),
                        affinity_class_limit=affinity_class_limit,
                        named_only=named_only,

```
