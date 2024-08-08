# Description
Enumerate and process PMIDs to extend a model and analyze the types of content processed.

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
					logger.warning('Invalid PMID: %s' % ev.pmid)

try:
	import boto3
	from indra_reading.scripts.submit_reading_pipeline import submit_reading, BatchMonitor
	aws_available = True
except Exception:
	aws_available = False

def process_paper_helper(model_name, pmid, start_time_local):
	try:
		if not aws_available:
			rp, txt_format = process_paper(model_name, pmid)
		else:
			rp, txt_format = process_paper_aws(pmid, start_time_local)
	except:
		logger.exception('uncaught exception while processing %s', pmid)
		return None, None

def extend_model(model_name, model, pmids, start_time_local):
    npapers = 0
    nabstracts = 0
    nexisting = 0

    # Preprocess PMID search results
    pmids_inv = defaultdict(list)
    for search_term, pmid_list in pmids.items():
        for pmid in pmid_list:
            if pmid in model.stmts:
                continue
            pmids_inv[pmid].append(search_term)

    logger.info('Found %d unique and novel PMIDS', len(pmids_inv))

    if not os.path.exists(os.path.join(model_name, 'jsons')):
        os.mkdir(os.path.join(model_name, 'jsons'))

    for counter, (pmid, search_terms) in enumerate(pmids_inv.items(), start=1):
        logger.info('[%d/%d] Processing %s for search terms: %s',
                    counter, len(pmids_inv), pmid, search_terms)

        rp, txt_format = process_paper_helper(model_name, pmid,
                                              start_time_local)

        if rp is None:
            logger.info('Reach processing failed for PMID%s', pmid)
            continue

        if txt_format == 'abstract':
            nabstracts += 1
        elif txt_format in ['pmc_oa_xml', 'elsevier_xml']:
            npapers += 1
        else:
            nexisting += 1

        if not rp.statements:
            logger.info('No statement from PMID%s (%s)' %
                        (pmid, txt_format))
        else:
            logger.info('%d statements from PMID%s (%s)' %
                        (len(rp.statements), pmid, txt_format))
        model.add_statements(pmid, rp.statements)


```
