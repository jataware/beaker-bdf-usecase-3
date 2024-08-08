# Description
Test example demonstrating how to process a JSON string with errors in agent definitions using the `sparser.process_json_dict` function.

# Code
```
import json
from indra.sources import sparser
from indra.sources.sparser.processor import fix_agent
from indra.statements import Agent, Phosphorylation, Complex
json_str2 = '[
{
"type": "Phosphorylation",
"evidence": [
{
"source_api": "sparser",
"text": "MEK phosphorylates ERK",
"pmid": "PMC_3500"}],
"sub": "ERK",
"enz": {
"name": "MEK",
"db_refs": {
"FPLX": "MEK",
"TEXT": "MEK"},
"TEXT": "MEK"}},
{
"type": "Complex",
"members": [
"MEK",
{
"name": "ERK",
"db_refs": {"FPLX": "ERK",
"TEXT": "ERK"}}],
"belief": 1,
"id": "3eedc7a9-fbbd-4e2e-b227-07d96f4bcff5"}

def test_process_json_str_with_bad_agents():
    sp = sparser.process_json_dict(json.loads(json_str2))
    assert sp is not None
    assert len(sp.statements) == 1, len(sp.statements)
    assert isinstance(sp.statements[0], Phosphorylation)
    assert len(sp.extraction_errors) == 1

```
