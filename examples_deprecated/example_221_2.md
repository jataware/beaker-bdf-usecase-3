# Description
Process UbiBrowser data from files.

# Code
```
import pandas

def process_file(e3_path: str, dub_path: str) -> UbiBrowserProcessor:
    """Process UbiBrowser data from files.

    Parameters
    ----------
    e3_path :
        The path to the E3 file.
    dub_path :
        The path to the DUB file.

    Returns
    -------
    :
        An UbiBrowserProcessor object with INDRA Statements
        extracted in its statements attribute.
    """
    e3_df = pandas.read_csv(e3_path, sep='\t')
    dub_df = pandas.read_csv(dub_path, sep='\t')

```
