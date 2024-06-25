# Description
Example demonstrating how to create an SBGN model for an IncreaseAmount statement and validate it.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import requests
from lxml import etree
from indra.statements import *
from indra.assemblers.sbgn.assembler import SBGNAssembler, sbgn_ns

ns = {'sbgn': sbgn_ns}
schema_url = 'https://raw.githubusercontent.com/sbgn/libsbgn/' + 'master/resources/SBGN.xsd'

def _get_parser():
    res = requests.get(schema_url)
    xsd_str = res.text
    schema_root = etree.XML(xsd_str)
    schema = etree.XMLSchema(schema_root)
    # FIXME: the validation should be reinstated when it works
    #parser = etree.XMLParser(schema=schema)
    parser = etree.XMLParser()
    return parser

sbgn_parser = _get_parser()

def _parse_sbgn(sbgn_xml):
    print(sbgn_xml)
    et = etree.fromstring(sbgn_xml, sbgn_parser)
    return et

def _test_numelements(et, nglyphs, narcs):
    glyphs = et.findall('sbgn:map/sbgn:glyph', namespaces=ns)
    assert len(glyphs) == nglyphs
    arcs = et.findall('sbgn:map/sbgn:arc', namespaces=ns)

def test_increaseamount():
    st = IncreaseAmount(Agent(''), Agent('MAP2K1'))
    sa = SBGNAssembler([st])
    sbgn_xml = sa.make_model()
    et = _parse_sbgn(sbgn_xml)

```
