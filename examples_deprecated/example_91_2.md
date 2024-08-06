# Description
Save an HTML model with statements and verify colors.

# Code
```
import re
from indra.assemblers.english import AgentWithCoordinates
from indra.assemblers.html.assembler import HtmlAssembler, tag_text, loader, _format_evidence_text, tag_agents, src_url, SOURCE_INFO, DEFAULT_SOURCE_COLORS, generate_source_css, _source_info_to_source_colors, SourceInfo
from indra.resources import load_resource_json
from indra.statements import *

def test_colors_in_html():
    ag_a = Agent('A')
    ag_b = Agent('B')
    evidences = []
    colors = []
    for source_type, info in DEFAULT_SOURCE_COLORS:
        for source in info['sources']:
            ev = Evidence(source_api=source, text=f'Evidence from {source}')
            evidences.append(ev)
            colors.append(info['sources'][source])

    stmt = Activation(ag_a, ag_b, evidence=evidences)
    ha = HtmlAssembler(statements=[stmt])
    ha.save_model('./temp_simple.html')
    ha = HtmlAssembler(statements=[stmt])
    ha.save_model('./temp_not_simple.html', simple=False)
    with open('./temp_simple.html') as fh:
        simple_html = fh.read()
    with open('./temp_not_simple.html') as fh:
        not_simple_html = fh.read()
    assert all(color in simple_html for color in colors)

```
