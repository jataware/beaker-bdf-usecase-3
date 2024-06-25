# Description
Test fetching mutations for BRAF and AKT1 genes in specific cell lines and verifying the mutation data.

# Code
```
import pytest

@pytest.mark.webservice
def test_get_ccle_mutations():
    muts = cbio_client.get_ccle_mutations(['BRAF', 'AKT1'],
                                          ['LOXIMVI_SKIN', 'A101D_SKIN'])
    assert len([x for x in muts]) == 2
    assert 'V600E' in muts['LOXIMVI_SKIN']['BRAF']
    assert 'V600E' in muts['A101D_SKIN']['BRAF']
    assert 'I208V' in muts['LOXIMVI_SKIN']['BRAF']
    assert 'I208V' not in muts['A101D_SKIN']['BRAF']
    assert len(muts['LOXIMVI_SKIN']['AKT1']) == 0

```
