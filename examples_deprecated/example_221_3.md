# Description
Process data frames containing UbiBrowser data.

# Code
```
import pandas

def process_df(e3_df: pandas.DataFrame, dub_df: pandas.DataFrame) \
        -> UbiBrowserProcessor:
    """Process data frames containing UbiBrowser data.

    Parameters
    ----------
    e3_df :
        A data frame containing UbiBrowser E3 data.
    dub_df :
        A data frame containing UbiBrowser DUB data.

    Returns
    -------
    :
        An UbiBrowserProcessor object with INDRA Statements
        extracted in its statements attribute.
    """
    up = UbiBrowserProcessor(e3_df, dub_df)
    up.extract_statements()

```
