# Description
Submit processing jobs to AWS and monitor their completion, then load and extend a machine learning model with new statements derived from PMIDs.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import os
import logging
import time
import datetime
import tzlocal
from collections import defaultdict
from indra.sources import reach
from indra.databases import ndex_client
from indra.tools.assemble_corpus import filter_db_highbelief
from indra.tools.incremental_model import IncrementalModel
from indra.assemblers.cx import CxAssembler
from indra.tools.machine import twitter_client
logger = logging.getLogger(__name__)
def upload_new_ndex(model_path, new_stmts, ndex_cred):	
	logger.info('Uploading to NDEx')
	logger.info(time.strftime('%c'))
	cx_str = assemble_cx(new_stmts, name=ndex_cred.get('name', 'rasmachine'))
	cx_name = os.path.join(model_path, 'model.cx')
	with open(cx_name, 'wb') as fh:
		fh.write(cx_str.encode('utf-8'))
	upload_cx_to_ndex(cx_str, ndex_cred)
def upload_cx_to_ndex(cx_str, ndex_cred):
	ndex_client.update_network(cx_str, ndex_cred['network'], ndex_cred)
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

def run_machine(model_path, pmids, belief_threshold, search_genes=None,
                ndex_cred=None, twitter_cred=None, grounding_map=None):
    start_time_local = datetime.datetime.now(tzlocal.get_localzone())
    date_str = make_date_str()

    # Save PMIDs in file and send for remote reading
    if aws_available:
        pmid_fname = 'pmids-%s.txt' % date_str
        all_pmids = []
        for v in pmids.values():
            all_pmids += v
        all_pmids = list(set(all_pmids))

        with open(pmid_fname, 'wt') as fh:
            for pmid in all_pmids:
                fh.write('%s\n' % pmid)
        # Submit reading
        job_list = submit_reading('rasmachine', pmid_fname, ['reach'])

        # Wait for reading to complete
        monitor = BatchMonitor('run_reach_queue', job_list)
        monitor.watch_and_wait(idle_log_timeout=600, kill_on_log_timeout=True)

    # Load the model
    logger.info(time.strftime('%c'))
    logger.info('Loading original model.')
    inc_model_file = os.path.join(model_path, 'model.pkl')
    model = IncrementalModel(inc_model_file)
    # Include search genes as prior genes
    if search_genes:
        model.prior_genes = search_genes
    stats = {}
    logger.info(time.strftime('%c'))
    logger.info('Preassembling original model.')
    model.preassemble(filters=global_filters, grounding_map=grounding_map)
    logger.info(time.strftime('%c'))

    # Original statistics
    stats['orig_stmts'] = len(model.get_statements())
    stats['orig_assembled'] = len(model.assembled_stmts)
    orig_stmts = filter_db_highbelief(model.assembled_stmts, ['bel', 'biopax'],
                                      belief_threshold)
    orig_stmts = ac.filter_top_level(orig_stmts)
    stats['orig_final'] = len(orig_stmts)
    logger.info('%d final statements' % len(orig_stmts))

    # Extend the model with PMIDs
    logger.info('----------------')
    logger.info(time.strftime('%c'))
    logger.info('Extending model.')
    stats['new_papers'], stats['new_abstracts'], stats['existing'] = \
        extend_model(model_path, model, pmids, start_time_local)
    # Having added new statements, we preassemble the model
    model.preassemble(filters=global_filters, grounding_map=grounding_map)

    # New statistics
    stats['new_stmts'] = len(model.get_statements())
    stats['new_assembled'] = len(model.assembled_stmts)
    new_stmts = filter_db_highbelief(model.assembled_stmts, ['bel', 'biopax'],
                                     belief_threshold)
    new_stmts = ac.filter_top_level(new_stmts)
    stats['new_final'] = len(new_stmts)
    logger.info('%d final statements' % len(new_stmts))

    check_pmids(model.get_statements())

    # Save model
    logger.info(time.strftime('%c'))
    logger.info('Saving model')
    model.save(inc_model_file)
    logger.info(time.strftime('%c'))

    # Save a time stamped version of the pickle for backup/diagnostic purposes
    if not aws_available:
        inc_model_bkp_file = os.path.join(model_path,
                                          'model-%s.pkl' % date_str)
        model.save(inc_model_bkp_file)
    else:
        key = 'rasmachine/%s/model-%s.pkl' % (model_path.replace('/', '_'),
                                              date_str)
        s3 = boto3.client('s3')
        s3.upload_file(inc_model_file, 'bigmech', key)

    # Upload the new, final statements to NDEx
    if ndex_cred:
        upload_new_ndex(model_path, new_stmts, ndex_cred)

    # Print and tweet the status message
    logger.info('--- Final statistics ---')
    for k, v in sorted(stats.items(), key=lambda x: x[0]):
        logger.info('%s: %s' % (k, v))
    logger.info('------------------------')

    msg_str = make_status_message(stats)
    if msg_str is not None:
        logger.info('Status message: %s' % msg_str)
        if twitter_cred:
            logger.info('Now tweeting: %s' % msg_str)

```
