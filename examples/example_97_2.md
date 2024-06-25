# Description
Process a text mentioning a phosphorylation event and verify the extracted statements of type Phosphorylation.

# Code
```
from indra.sources.isi.api import process_text

def test_process_phosphorylation():
    # Include a sentence without a mechanism to test ISI's ability to
    # associate the relevant sentence text with an extracted event.
    ip = process_text('This sentence is false. Ras phosphorylates Raf.', '42')

    statements = ip.statements
    assert len(statements) == 1

    s0 = statements[0]
    assert type(s0) == Phosphorylation

    enz = s0.enz
    assert enz.name == 'RAS'
    assert enz.db_refs['TEXT'] == 'Ras'
    assert enz.db_refs['FPLX'] == 'RAS'

    sub = s0.sub
    assert sub.name == 'RAF'
    assert sub.db_refs['TEXT'] == 'Raf'
    assert sub.db_refs['FPLX'] == 'RAF'

    assert len(s0.evidence) == 1
    ev = s0.evidence[0]
    assert ev.source_api == 'isi'
    assert ev.pmid == '42'
    assert ev.text == 'Ras phosphorylates Raf.'
    assert ev.annotations['interaction'] == ['phosphorylates', 'Ras', 'Raf']
    assert ev.annotations['source_id'] is not None

    ip.retain_molecular_complexes()

```
