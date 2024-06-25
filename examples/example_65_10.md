# Description
Test fetching CNA data on multiple genes in several cell lines and ensuring the data is retrieved correctly.

# Code
```
import pytest

@pytest.mark.webservice
def test_get_ccle_cna_big():
    """
    Get the CNA data on 124 genes in 4 cell lines. Expect to have CNA values
    that are {-2.0, -1.0, 0.0, 1.0, 2.0}. This tests the function at
    a greater scale. Also, test the cell lines' BRAF CNAs
    """
    genes = ["FOSL1", "GRB2", "RPS6KA3", "EIF4EBP1", "DUSP1", "PLXNB1", "SHC2",
             "CBL", "E2F2", "KRAS", "RPS6KA1", "AKT2", "PRKAG2", "JUN", "ELK1",
             "MTOR", "PPP1CA", "TP73", "PIK3R1", "PIK3CG", "FOS", "MLST8",
             "FGFR3", "PRKAG1", "RAF1", "PIK3CA", "TSC1", "AKT3", "SAV1",
             "CCND1", "ETS1", "EXOC7", "CBLB", "MAP2K2", "CDC25A", "PEA15",
             "YAP1", "IRS1", "RPS6KA6", "SOS1", "MDM2", "PIK3R6", "PIK3R2",
             "RASSF1", "AKT1", "BUB1", "PRKAB2", "ETS2", "PRKAG3", "CDK2",
             "TP53", "DAB2IP", "MAPK3", "CDK4", "PRKAB1", "CDK6", "PIK3R5",
             "PAK3", "MYC", "INSR", "SHOC2", "CDKN1A", "STK4", "STK11",
             "RPS6KB1", "RPS6KA2", "KSR1", "PIN1", "MAPK1", "E2F1", "RAC1",
             "CDC6", "EGFR", "NFE2L2", "SHC3", "PTPN11", "PIK3R3", "SHC4",
             "ROCK2", "RPTOR", "CCNA2", "HRAS", "TSC2", "BRCA2", "ALK",
             "MAP2K1", "BRIP1", "CBLC", "RHOA", "RPS6KB2", "FGFR2", "FGFR1",
             "ERBB2", "SOS2", "PRKAA1", "TIAM1", "MET", "PRKAA2", "ROS1",
             "TBK1", "RB1", "PEBP1", "DUSP6", "PTEN", "PDPK1", "MRAS", "NRAS",
             "BRAF", "STK3", "CCNA1", "NFKB1", "CCND3", "PAK4", "KSR2", "ECT2",
             "BRCA1", "VAV1", "CCND2", "ARAF", "PAK2", "PIK3CD", "SHC1",
             "PAK1", "RHEB"]
    cell_lines = ['COLO679_SKIN', 'A2058_SKIN', 'IGR39_SKIN', 'HS294T_SKIN']
    cna = cbio_client.get_ccle_cna(genes, cell_lines)
    values = set()
    for cl in cna:
        for g in cna[cl]:
            values.add(cna[cl][g])
    assert values == {-2.0, -1.0, 0.0, 1.0, 2.0}
    assert cna['COLO679_SKIN']['BRAF'] == 2
    assert cna['A2058_SKIN']['BRAF'] == 1
    assert cna['IGR39_SKIN']['BRAF'] == 1

```
