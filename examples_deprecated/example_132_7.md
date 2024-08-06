# Description
Test example demonstrating how to process JSON string representing a phosphorylation event using the `sparser.process_json_dict` function.

# Code
```
import json
from indra.sources import sparser
from indra.sources.sparser.processor import fix_agent
from indra.statements import Agent, Phosphorylation, Complex
json_str1 = '[
{
"type": "Phosphorylation",
"evidence": [
{
"source_api": "sparser",
"text": "MEK phosphorylates ERK",
"pmid": "PMC_3500"}],
"sub": {
"name": "ERK",
"db_refs": {
"NCIT": "C26360",
"TEXT": "ERK"},
"TEXT": "ERK"},
"enz": {
"name": "MEK",
"db_refs": {
"FPLX": "MEK",
"TEXT": "MEK"},
"TEXT": "MEK"}
}

def test_process_json_str():
    sp = sparser.process_json_dict(json.loads(json_str1))
    assert sp is not None
    assert len(sp.statements) == 1
    assert isinstance(sp.statements[0], Phosphorylation)
    sp.set_statements_pmid('1234567')
    assert sp.statements[0].evidence[0].pmid == '1234567'

```
