# Description
Formatting evidence text into a dictionary with specific keys.

# Code
```
import re
from indra.assemblers.english import AgentWithCoordinates
from indra.assemblers.html.assembler import HtmlAssembler, tag_text, loader, _format_evidence_text, tag_agents, src_url, SOURCE_INFO, DEFAULT_SOURCE_COLORS, generate_source_css, _source_info_to_source_colors, SourceInfo
from indra.resources import load_resource_json
from indra.statements import *
from indra.util.statement_presentation import AveAggregator, StmtStat, internal_source_mappings

def make_stmt():
    src = Agent('SRC', db_refs={'HGNC': '11283'})
    ras = Agent('RAS', db_refs={'FPLX': 'RAS'})
    ev = Evidence(text="We noticed that the Src kinase was able to phosphorylate Ras proteins.", source_api='test', pmid='1234567', annotations={'agents': {'raw_text': ['Src kinase', 'Ras proteins']}, 'source_url': 'http://www.causalbionet.com/'})
    st = Phosphorylation(src, ras, 'tyrosine', '32', evidence=[ev])

def test_format_evidence_text():
    stmt = make_stmt()
    ev_list = _format_evidence_text(stmt)
    assert len(ev_list) == 1
    ev = ev_list[0]
    assert isinstance(ev, dict)
    assert set(ev.keys()) == {'source_api', 'text_refs', 'text', 'source_hash',
                              'pmid', 'num_curations', 'num_correct',
                              'num_incorrect', 'original_json', 'source_url'}
    assert ev['source_api'] == 'test'
    assert ev['text_refs']['PMID'] == '1234567'
    assert ev['text'] == ('We noticed that the '
                          '<span class="badge badge-subject">Src kinase</span> '
                          'was able to phosphorylate '
                          '<span class="badge badge-object">'

```
