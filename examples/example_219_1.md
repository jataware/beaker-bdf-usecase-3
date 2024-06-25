# Description
Demonstrates how to download a table from a specified URL and process it into a TrrustProcessor object.

# Code
```
import io
import pandas
import logging
import requests
from .processor import TrrustProcessor

trrust_human_url = 'https://www.grnpedia.org/trrust/data/trrust_rawdata.human.tsv'


def process_from_web():
    """Return a TrrustProcessor based on the online interaction table.

    Returns
    -------
    TrrustProcessor
        A TrrustProcessor object that has a list of INDRA Statements in its
        statements attribute.
    """
    logger.info('Downloading table from %s' % trrust_human_url)
    res = requests.get(trrust_human_url)
    res.raise_for_status()
    df = pandas.read_table(io.StringIO(res.text))
    tp = TrrustProcessor(df)
    tp.extract_statements()

```
