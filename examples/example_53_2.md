# Description
Test the fplx_lookup functionality of the AcsnProcessor.

# Code
```
import requests
from indra.sources.acsn import api
from indra.sources.acsn.processor import AcsnProcessor

relations_df = pandas.read_csv(api.ACSN_RELATIONS_URL, sep='\t')
gmt_file = requests.get(api.ACSN_CORRESPONDENCE_URL).text.split('\n')
correspondence_dict = api._transform_gmt(gmt_file)

def test_famplex_lookup():
    fplx_lookup = ap.fplx_lookup
    assert 'USPL' in fplx_lookup[('CYLD', 'USPL1')]

```
