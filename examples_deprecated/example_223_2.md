# Description
Process a TSV data file obtained from VirHostNet and return a VirhostnetProcessor object containing extracted INDRA Statements.

# Code
```
import pandas
import logging
from .processor import VirhostnetProcessor

data_columns = [
    'host_grounding', 'vir_grounding', 'host_mnemonic', 'vir_mnemonic',
    'host_mnemonic2', 'vir_mnemonic2', 'exp_method',
    'dash', 'publication', 'host_tax', 'vir_tax',
    'int_type', 'source', 'source_id', 'score'
]

def process_df(df, up_web_fallback=False):
    """Process a VirHostNet pandas DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        A DataFrame representing VirHostNet interactions (in the same format as
        the web service).

    Returns
    -------
    VirhostnetProcessor
        A VirhostnetProcessor object which contains a list of extracted
        INDRA Statements in its statements attribute.
    """
    vp = VirhostnetProcessor(df, up_web_fallback=up_web_fallback)
    vp.extract_statements()

def process_tsv(fname, up_web_fallback=False):
    """Process a TSV data file obtained from VirHostNet.

    Parameters
    ----------
    fname : str
        The path to the VirHostNet tabular data file (in the same format as
        the web service).

    Returns
    -------
    VirhostnetProcessor
        A VirhostnetProcessor object which contains a list of extracted
        INDRA Statements in its statements attribute.
    """
    df = pandas.read_csv(fname, delimiter='\t', names=data_columns,
                         header=None)

```
