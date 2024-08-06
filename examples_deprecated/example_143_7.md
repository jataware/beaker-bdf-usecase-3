# Description
Processing a single row of data using 'process_row' function and validating the generated statement.

# Code
```
from indra.sources.virhostnet.processor import process_row
from indra.statements import Complex

# Define test row for processing
test_row_str = ('uniprotkb:Q6P5R6\tuniprotkb:Q1K9H5\t'
                 'uniprotkb:RL22L_HUMAN\tuniprotkb:Q1K9H5_I33A0\t'
                 'uniprotkb:RL22L_HUMAN\tuniprotkb:Q1K9H5_I33A0\t'
                 'psi-mi:"MI:0004"(affinity chromatography technology)\t'
                 '-\tpubmed:26651948\ttaxid:9606\ttaxid:381518\t'
                 'psi-mi:"MI:0915"(physical association)\t'
                 'psi-mi:"MI:1114"(virhostnet)\t'
                 'virhostnet-rid:19809|virhostnet-nrid:18603\t'
                 'virhostnet-miscore:0.32715574')

def test_process_row():
    stmt = process_row(test_row)

```
