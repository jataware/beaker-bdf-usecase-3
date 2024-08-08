# Description
Process a VirHostNet pandas DataFrame and return a VirhostnetProcessor object containing extracted INDRA Statements.

# Code
```
pandas
logging

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

```
