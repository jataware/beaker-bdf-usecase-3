# Description
How to process RLIMSP extractions from a bulk-download JSON-L file.

# Code
```
import json

def process_jsonl_file(filename, doc_id_type=None):
    """Process RLIMSP extractions from a bulk-download JSON-L file.

    Parameters
    ----------
    filename : str
        Path to the JSON file.
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
    with open(filename, 'rt') as f:
        json_list = [json.loads(line) for line in f.readlines()]
        rp = RlimspProcessor(json_list, doc_id_type=doc_id_type)
        rp.extract_statements()

```
