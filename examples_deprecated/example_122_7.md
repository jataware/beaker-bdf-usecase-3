# Description
Test phosphorylation with no enzyme using PysbAssembler.

# Code
```
import xml.etree.ElementTree as ET
from indra.assemblers.pysb import PysbAssembler
import indra.assemblers.pysb.assembler as pa
from indra.statements import Agent, Complex, Phosphorylation
from pysb import bng, WILD, Monomer, Annotation
from pysb.testing import with_model
import pytest
from indra.assemblers.pysb.export import export_cm_network

def test_pysb_assembler_phos_noenz():
    enz = None
    sub = Agent('MEK1')
    stmt = Phosphorylation(enz, sub, 'serine', '222')
    pa = PysbAssembler([stmt])
    model = pa.make_model()
    assert len(model.rules) == 0

```
