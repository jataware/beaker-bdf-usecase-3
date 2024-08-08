# Description
Check if the parsed XML elements contain unicode strings using the custom UnicodeXMLTreeBuilder parser.

# Code
```
io import BytesIO
xml.etree.ElementTree as ET
indra.util import unicode_strs

def test_unicode_tree_builder():
    xml = u'<html><bar>asdf</bar></html>'.encode('utf-8')
    xml_io = BytesIO(xml)
    tree = ET.parse(xml_io, parser=UTB())
    bar = tree.find('.//bar')

```
