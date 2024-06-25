# Description
Download the UbiBrowser data from the web and process it.

# Code
```
import pandas
from .processor import UbiBrowserProcessor

DOWNLOAD_URL = 'http://ubibrowser.bio-it.cn/ubibrowser_v3/Public/download/literature/'
E3_URL = DOWNLOAD_URL + 'literature.E3.txt'

def process_from_web() -> UbiBrowserProcessor:
    """Download the UbiBrowser data from the web and process it.

    Returns
    -------
    :
        An UbiBrowserProcessor object with INDRA Statements
        extracted in its statements attribute.
    """
    e3_df = pandas.read_csv(E3_URL, sep='\t')
    dub_df = pandas.read_csv(DUB_URL, sep='\t')

```
