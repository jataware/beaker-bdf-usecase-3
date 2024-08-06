# Description
Assemble an HTML model from statements.

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
    return st

def make_bad_stmt():
    subj = None  # None agent
    ras = Agent('', db_refs={'FPLX': {'RAS', 'Ras'}, 'TEXT': 'RAS'})
    ev = Evidence(text="Ras is phosphorylated", source_api='test', pmid='1234', annotations={'agents': {'raw_text': [None, None]},  # no raw
                            'source_url': ''})
    st = Phosphorylation(subj, ras, 'tyrosine', '32', evidence=[ev])

def test_assembler():
    stmt = make_stmt()
    ha = HtmlAssembler([stmt])
    result = ha.make_model()
    assert isinstance(result, str)
    # Read from the template file and make sure the beginning and end of the
    # content matches
    template, _, _ = loader.get_source(None, 'indra/template.html')
    assert result.startswith(template[0:100])
    # Make sure assembler works with other parameters provided
    stmt2 = make_bad_stmt()
    ha = HtmlAssembler(
        source_counts={stmt.get_hash(): {'test': 1},
                       stmt2.get_hash(): {'test': 1}},
        ev_counts={stmt.get_hash(): 1, stmt2.get_hash(): 1},
        db_rest_url='test.db.url')
    ha.add_statements([stmt, stmt2])
    result = ha.make_model(grouping_level='agent-pair')
    assert isinstance(result, str)
    result = ha.make_model(grouping_level='statement')
    assert isinstance(result, str)
    # Check simple=False
    result = ha.make_model(grouping_level='statement', simple=False)
    assert isinstance(result, str)
    # Test belief badges
    result = ha.make_model(grouping_level='statement', show_belief=True)
    assert isinstance(result, str)
    assert '<small\n' \
           '      class="badge badge-pill badge-belief"\n' \
           '      title="Belief score for this statement">1.0</small>' in result
    result = ha.make_model(grouping_level='statement', show_belief=False)
    assert isinstance(result, str)
    assert '<small\n' \
           '      class="badge badge-pill badge-belief"\n' \
           '      title="Belief score for this statement">1</small>' \
           not in result
    # Test if source URL exists
    assert 'http://www.causalbionet.com/' in result
    # Make sure warning can be appended
    ha.append_warning('warning')
    assert ('\t<span style="color:red;">(CAUTION: warning occurred when '
            'creating this page.)</span>' in ha.model)
    # Make sure model is created before saving
    ha = HtmlAssembler([stmt])
    assert not ha.model
    ha.save_model('tempfile.html')

```
