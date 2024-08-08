# Description
Processing DataFrame using 'virhostnet.process_df' function and validating the statement.

# Code
```
import pandas
from indra.sources.virhostnet.api import data_columns
from indra.sources.virhostnet.processor import process_row

test_row_str = ('uniprotkb:Q6P5R6	uniprotkb:Q1K9H5	'
                 'uniprotkb:RL22L_HUMAN	uniprotkb:Q1K9H5_I33A0	'
                 'uniprotkb:RL22L_HUMAN	uniprotkb:Q1K9H5_I33A0	'
                 'psi-mi:"MI:0004"(affinity chromatography technology)	'
                 '-	pubmed:26651948	taxid:9606	taxid:381518	'
                 'psi-mi:"MI:0915"(physical association)	'
                 'psi-mi:"MI:1114"(virhostnet)	'
                 'virhostnet-rid:19809|virhostnet-nrid:18603	'
                 'virhostnet-miscore:0.32715574')
test_row = {k: v for k, v in zip(data_columns, test_row_str.split('\t'))}

def test_process_df():
    vp = virhostnet.process_df(test_df)
    assert len(vp.statements) == 1

```
