# Description
Testing the make_repository_component function of the BMI model

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

def test_make_repo_component():
    bm = make_bmi_model()
    bm.model.name = 'indra_model'
    comp = bm.make_repository_component()
    print(comp)

```
