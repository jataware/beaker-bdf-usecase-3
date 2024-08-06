# Description
Process a text mentioning a protein complex and verify the extracted statements of type Complex.

# Code
```
from indra.sources.isi.api import process_text

def test_process_complex():
    ip = process_text('Ras binds to Raf.', '42')

    statements = ip.statements
    assert len(statements) == 1

    s0 = statements[0]
    assert type(s0) == Complex

    assert len(s0.members) == 2

    m0 = s0.members[0]
    assert m0.name == 'RAS', m0
    assert m0.db_refs['TEXT'] == 'Ras', m0.db_refs
    assert m0.db_refs['FPLX'] == 'RAS', m0.db_refs

    m1 = s0.members[1]
    assert m1.name == 'RAF', m1
    assert m1.db_refs['TEXT'] == 'Raf', m1.db_refs
    assert m1.db_refs['FPLX'] == 'RAF', m1.db_refs

    assert len(s0.evidence) == 1
    ev = s0.evidence[0]
    assert ev.source_api == 'isi'
    assert ev.pmid == '42'
    assert ev.text == 'Ras binds to Raf.'
    assert ev.annotations['interaction'] == ['binds', None, 'Ras', 'Raf']
    assert ev.annotations['source_id'] is not None
    ip.retain_molecular_complexes()

```
