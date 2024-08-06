# Description
Demonstrates processing a natural language description of a mechanism using TRIPS and assembling the mechanism using PysbAssembler.

# Code
```
from indra.sources import trips

def test_readme_using_indra1():
    from indra.sources import trips
    from indra.assemblers.pysb import PysbAssembler
    pa = PysbAssembler()
    # Process a natural language description of a mechanism
    trips_processor = trips.process_text(
        'MEK2 phosphorylates ERK1 at Thr-202 and Tyr-204')
    # Collect extracted mechanisms in PysbAssembler
    pa.add_statements(trips_processor.statements)
    # Assemble the model
    model = pa.make_model(policies='two_step')

```
