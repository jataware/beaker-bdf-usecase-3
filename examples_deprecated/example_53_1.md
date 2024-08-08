# Description
Test the _transform_gmt function of the ACSN API.

# Code
```
import requests
from indra.sources.acsn import api
from indra.sources.acsn.processor import AcsnProcessor

relations_df = pandas.read_csv(api.ACSN_RELATIONS_URL, sep='\t')
gmt_file = requests.get(api.ACSN_CORRESPONDENCE_URL).text.split('\n')
correspondence_dict = api._transform_gmt(gmt_file)

def test_transform_gmt():
    gmt_dict = api._transform_gmt(gmt_file)
    assert 'C3' in gmt_dict['C3B*']
    assert 'ZO4*' not in gmt_dict
    assert not gmt_dict['SLC2A1'][0].endswith('\t')

```
