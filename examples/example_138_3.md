# Description
Example demonstrating the processing of a text to extract a ubiquitination statement using the INDRA library

# Code
```
from os.path import dirname, join
import indra.statements as ist
from indra.sources import trips
from indra.util import unicode_strs
import pytest

test_small_file = join(dirname(__file__), 'test_small.xml')

def assert_if_hgnc_then_up(st):
    agents = st.agent_list()
    for a in agents:
        if a is not None:
            up_id = a.db_refs.get('UP')
            hgnc_id = a.db_refs.get('HGNC')
            if hgnc_id and not up_id:
                assert False


def assert_grounding_value_or_none(st):
    agents = st.agent_list()
    for a in agents:
        if a is not None:
            for k, v in a.db_refs.items():
                if not v:

@pytest.mark.slow
def test_ubiquitination():
    tp = trips.process_text('MDM2 ubiquitinates TP53.')
    assert len(tp.statements) == 1
    st = tp.statements[0]
    assert isinstance(st, ist.Ubiquitination)
    assert unicode_strs((tp, st))
    assert_grounding_value_or_none(st)
    assert_if_hgnc_then_up(st)

```
