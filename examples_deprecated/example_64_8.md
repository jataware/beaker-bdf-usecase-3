# Description
Testing the get_attribute function of the BMI model

# Code
```
from indra.statements import *
from indra.assemblers.pysb import PysbAssembler
from indra.assemblers.pysb.bmi_wrapper import BMIModel

stmts = [Influence(Event(Concept('rainfall')),
                   Event(Concept('flood'))),
         Influence(Event(Concept('flood')),
                   Event(Concept('displacement')))]

def make_bmi_model():
    pa = PysbAssembler()
    pa.add_statements(stmts)
    model = pa.make_model()
    bm = BMIModel(model, inputs=['rainfall'])

def test_get_attribute():
    bm = make_bmi_model()
    attr = bm.get_attribute('model_name')

```
