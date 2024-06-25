# Description
How to process RLIMSP extractions from a JSON-L string.

# Code
```
import json

def process_jsonl_str(jsonl_str, doc_id_type=None):
    """Process RLIMSP extractions from a JSON-L string.

    Parameters
    ----------
    jsonl_str : str
        The contents of one of the JSON-L files you can find here:
        https://hershey.dbi.udel.edu/textmining/export
    doc_id_type : Optional[str]
        In some cases the RLIMS-P paragraph info doesn't contain 'pmid' or
        'pmcid' explicitly, instead if contains a 'docId' key. This parameter
        allows defining what ID type 'docId' sould be interpreted as. Its
        values should be 'pmid' or 'pmcid' or None if not used.

    Returns
    -------
    :py:class:`indra.sources.rlimsp.processor.RlimspProcessor`
        An RlimspProcessor which contains a list of extracted INDRA Statements
        in its statements attribute.
    """
    json_list = [json.loads(line) for line in jsonl_str.splitlines()]
    rp = RlimspProcessor(json_list, doc_id_type=doc_id_type)
    rp.extract_statements()

```
