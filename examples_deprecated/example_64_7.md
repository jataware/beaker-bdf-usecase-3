# Description
Testing the get_value function of the BMI model

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

def test_get_value():
    bm = make_bmi_model()
    bm.initialize()
    bm.set_value('rainfall', 10.0)
    val = bm.get_value('rainfall')

```
