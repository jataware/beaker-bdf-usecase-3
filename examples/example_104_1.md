# Description
Test for resolving URNs to database references using `_urn_to_db_refs` function.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname

def test_urn_to_db_refs():
    # Test resolving a subset of the urns that are used for grounding
    # The processor adds the TEXT property to the generated db_refs after
    # calling urn_to_db_refs

    # agi-cas
    urn1 = 'urn:agi-cas:89-73-6'
    db_refs_1, _ = _urn_to_db_refs(urn1)
    assert db_refs_1 == {'CHEBI': 'CHEBI:45615'}, db_refs_1

    # agi-llid
    urn2 = 'urn:agi-llid:9451'
    db_refs_2, hgnc_name = _urn_to_db_refs(urn2)
    assert db_refs_2 == {'HGNC': '3255', 'UP': 'Q9NZJ5'}
    assert hgnc_name == 'EIF2AK3'

    # agi-ncimorgan
    urn3 = 'urn:agi-ncimorgan:C0012144'
    db_refs_3, _ = _urn_to_db_refs(urn3)
    assert db_refs_3 == {'UMLS': 'C0012144'}

    # agi-nicmcelltype
    urn4 = 'urn:agi-ncimcelltype:C0242633'
    db_refs_4, _ = _urn_to_db_refs(urn4)
    assert db_refs_4 == {'UMLS': 'C0242633'}

    # agi-meshdist
    urn5 = 'urn:agi-meshdis:Paramyotonia%20Congenita'
    db_refs_5, _ = _urn_to_db_refs(urn5)
    assert db_refs_5 == {'MESH': 'D020967'}

    # agi-gocomplex
    urn6 = 'urn:agi-gocomplex:0005610'
    db_refs_6, _ = _urn_to_db_refs(urn6)
    assert db_refs_6 == {'GO': 'GO:0005610', 'FPLX': 'Laminin_332'}

    # agi-go
    urn7 = 'urn:agi-go:0001515'
    db_refs_7, _ = _urn_to_db_refs(urn7)
    assert db_refs_7 == {'GO': 'GO:0001515'}

    # agi-ncimtissue
    urn8 = 'urn:agi-ncimtissue:C0007807'
    db_refs_8, _ = _urn_to_db_refs(urn8)
    assert db_refs_8 == {'UMLS': 'C0007807'}

    # Do we ground to Famplex when there is a correspondence between a GO
    # id and a Famplex id?
    urn9 = 'urn:agi-go:0000776'
    db_refs_9, _ = _urn_to_db_refs(urn9)
    assert db_refs_9 == {'GO': 'GO:0000776', 'FPLX': 'Kinetochore'}

    # Do we ground to Famplex when there is a correspondence between a MESH
    # id and a Famplex id?
    urn10 = 'urn:agi-ncimcelltype:Actins'
    db_refs_10, _ = _urn_to_db_refs(urn10)
    assert db_refs_10 == {'MESH': 'D000199', 'FPLX': 'Actin'}

    # If the urn corresponds to an eccode, do we ground to famplex if that
    # eccode is in the Famplex equivalences table?
    urn11 = 'urn:agi-enz:1.1.1.1'
    db_refs_11, _ = _urn_to_db_refs(urn11)
    assert db_refs_11 == {'FPLX': 'ADH'}

    # Do we check the Famplex equivalences table to see if a raw Medscan URN
    # maps to a Famplex ID?
    urn11 = 'urn:agi-aopfc:0000105'
    db_refs_11, _ = _urn_to_db_refs(urn11)

```
