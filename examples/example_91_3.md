# Description
Save an HTML model with custom source colors.

# Code
```
import re
from indra.assemblers.english import AgentWithCoordinates
from indra.assemblers.html.assembler import HtmlAssembler, tag_text, loader, _format_evidence_text, tag_agents, src_url, SOURCE_INFO, DEFAULT_SOURCE_COLORS, generate_source_css, _source_info_to_source_colors, SourceInfo
from indra.resources import load_resource_json
from indra.statements import *

def test_custom_colors_in_html():
    ag_a = Agent('A')
    ag_b = Agent('B')
    custom_sources: SourceInfo = {
        "src_a": {
            "name": "Src A",
            "link": "https://example.com/src_a",
            "type": "reader",
            "domain": "general",
            "default_style": {
                "color": "white",
                "background-color": "blue"
            }
        },
        "src_b": {
            "name": "Src B",
            "link": "https://example.com/src_b",
            "type": "database",
            "domain": "general",
            "default_style": {
                "color": "black",
                "background-color": "#bebada"
            }
        },
    }

    evidences = []
    colors = []
    sources = []
    for source, source_info in custom_sources.items():
        sources.append(source)
        ev = Evidence(source_api=source, text=f'Evidence from {source}')
        evidences.append(ev)
        colors.append(source_info['default_style']['background-color'])

    stmt = Activation(ag_a, ag_b, evidence=evidences)
    ha = HtmlAssembler(statements=[stmt], custom_sources=custom_sources)
    ha.save_model('./temp_custom_colors_simple.html')
    with open('./temp_custom_colors_simple.html') as fh:
        simple_html = fh.read()

    ha = HtmlAssembler(statements=[stmt], custom_sources=custom_sources)
    ha.save_model('./temp_not_simple.html', simple=False)
    with open('./temp_custom_colors_simple.html') as fh:
        not_simple_html = fh.read()

    # Check if style rule appears
    assert all(color in simple_html for color in colors)

    # Test if badge appears
    badge_str = 'class="badge badge-source source-{src}"'

```
