# Description
Test getting URL from statements' evidence annotations.

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

def test_source_url():
    # Test getting URL from annotations
    stmt = make_stmt()
    url = src_url(stmt.evidence[0])
    assert url == 'http://www.causalbionet.com/'

    # Test getting from SOURCE_INFO
    ev = Evidence(source_api='trrust')
    url = src_url(ev)
    assert url == SOURCE_INFO['trrust']['link']

    # Test getting from source that needs reverse mapping
    ev = Evidence(source_api='vhn')  # vhn => virhostnet
    url = src_url(ev)

```
