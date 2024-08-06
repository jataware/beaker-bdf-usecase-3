# Description
Test active form creation using PysbAssembler.

# Code
```
import xml.etree.ElementTree as ET
from indra.assemblers.pysb import PysbAssembler
import indra.assemblers.pysb.assembler as pa
from indra.statements import Agent, Complex, ActiveForm, MutCondition
from pysb import bng, WILD, Monomer, Annotation
from pysb.testing import with_model
import pytest
from indra.assemblers.pysb.export import export_cm_network

def test_pysb_assembler_actsub():
    stmt = ActiveForm(Agent('BRAF', mutations=[MutCondition('600', 'V', 'E')]),
                      'activity', True)
    pa = PysbAssembler([stmt])
    model = pa.make_model(policies='two_step')
    assert len(model.rules) == 0

```
