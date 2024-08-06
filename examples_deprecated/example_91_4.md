# Description
Check sources not in evidences are excluded from the template.

# Code
```
import re
from indra.assemblers.english import AgentWithCoordinates
from indra.assemblers.html.assembler import HtmlAssembler, tag_text, loader, _format_evidence_text, tag_agents, src_url, SOURCE_INFO, DEFAULT_SOURCE_COLORS, generate_source_css, _source_info_to_source_colors, SourceInfo
from indra.resources import load_resource_json
from indra.statements import *

def test_skip_sources_not_in_evidences():
    # Check sources not in provided sources are excluded from generated template
    ag_a = Agent('A')
    ag_b = Agent('B')
    evidences = []
    colors = []
    not_in_html = []
    for source_type, info in DEFAULT_SOURCE_COLORS:
        for n, source in enumerate(info['sources']):
            # Only get 4 first sources for each type
            if n < 4:
                ev = Evidence(source_api=source, text=f'Evidence from {source}')
                evidences.append(ev)
                colors.append(info['sources'][source])
            else:
                not_in_html.append(source)
    stmt = Activation(ag_a, ag_b, evidence=evidences)
    ha = HtmlAssembler(statements=[stmt])
    ha.save_model('./temp_simple.html')
    with open('./temp_simple.html') as fh:
        simple_html = fh.read()

    ha = HtmlAssembler(statements=[stmt])
    ha.save_model('./temp_not_simple.html', simple=False)
    with open('./temp_not_simple.html') as fh:
        not_simple_no_show_html = fh.read()

    ha = HtmlAssembler(statements=[stmt])
    ha.save_model('./temp_not_simple_no_show.html',
                  show_only_available=True)
    with open('./temp_not_simple_no_show.html') as fh:
        not_simple_html = fh.read()
    assert all(color in simple_html for color in colors)
    assert all(color in not_simple_html for color in colors)

    badge_class = 'class="badge badge-source source-{src}"'
    assert all(badge_class.format(src=src) not in

```
