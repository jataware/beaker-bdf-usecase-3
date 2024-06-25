# Description
Process a paper by obtaining its full text and running it through the ReachProcessor to extract INDRA Statements.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import os
import logging
from indra.sources import reach
from indra.literature import pubmed_client, get_full_text, elsevier_client
from collections import defaultdict
import time
logger = logging.getLogger(__name__)
def check_pmids(stmts):
	for stmt in stmts:
		for ev in stmt.evidence:
			if ev.pmid is not None:
				if not ev.pmid.isdigit():

def process_paper(model_name, pmid):
    """Process a paper with the given pubmed identifier

    Parameters
    ----------
    model_name : str
        The directory for the INDRA machine
    pmid : str
        The PMID to process.

    Returns
    -------
    rp : ReachProcessor
        A ReachProcessor containing the extracted INDRA Statements
        in rp.statements.
    txt_format : str
        A string representing the format of the text
    """
    json_directory = os.path.join(model_name, 'jsons')
    json_path = os.path.join(json_directory, 'PMID%s.json' % pmid)

    if pmid.startswith('api') or pmid.startswith('PMID'):
        logger.warning('Invalid PMID: %s' % pmid)
    # If the paper has been read, use the json output file
    if os.path.exists(json_path):
        rp = reach.process_json_file(json_path, citation=pmid)
        txt_format = 'existing_json'
    # If the paper has not been read, download the text and read
    else:
        try:
            txt, txt_format = get_full_text(pmid, 'pmid')
        except Exception:
            return None, None

        if txt_format == 'pmc_oa_xml':
            rp = reach.process_nxml_str(txt, citation=pmid, offline=True,
                                        output_fname=json_path)
        elif txt_format == 'elsevier_xml':
            # Extract the raw text from the Elsevier XML
            txt = elsevier_client.extract_text(txt)
            rp = reach.process_text(txt, citation=pmid, offline=True,
                                    output_fname=json_path)
        elif txt_format == 'abstract':
            rp = reach.process_text(txt, citation=pmid, offline=True,
                                    output_fname=json_path)
        else:
            rp = None
    if rp is not None:
        check_pmids(rp.statements)

```
