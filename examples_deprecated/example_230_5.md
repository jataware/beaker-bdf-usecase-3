# Description
Helper to setup machine configuration and credentials, then run machine learning processes to update models with new data.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import os
import logging
import yaml
import time
import sys
import datetime
import tzlocal
from indra.sources import reach
from indra.databases import ndex_client
from indra.tools.incremental_model import IncrementalModel
from indra.assemblers.cx import CxAssembler
from indra.literature import pubmed_client, get_full_text, elsevier_client
from indra import get_config, has_config
logger = logging.getLogger(__name__)
def get_email_pmids(gmail_cred):
	mailbox = gmail_client.gmail_login(gmail_cred.get('user'), gmail_cred.get('password'))
	gmail_client.select_mailbox(mailbox, 'INBOX')
	num_days = int(gmail_cred.get('num_days', 10))
	logger.info('Searching last %d days of emails', num_days)
	pmids = gmail_client.get_message_pmids(mailbox, num_days)
	return pmids
try:
	import boto3
	from indra_reading.scripts.submit_reading_pipeline import submit_reading, BatchMonitor
	aws_available = True
except Exception:

def run_with_search_helper(model_path, config, num_days=None):
    logger.info('-------------------------')
    logger.info(time.strftime('%c'))

    if not os.path.isdir(model_path):
        logger.error('%s is not a directory', model_path)
        sys.exit()

    default_config_fname = os.path.join(model_path, 'config.yaml')

    if config:
        config = get_machine_config(config)
    elif os.path.exists(default_config_fname):
        logger.info('Loading default configuration from %s',
                    default_config_fname)
        config = get_machine_config(default_config_fname)
    else:
        logger.error('Configuration file argument missing.')
        sys.exit()

    # Probability cutoff for filtering statements
    default_belief_threshold = 0.95
    belief_threshold = config.get('belief_threshold')
    if belief_threshold is None:
        belief_threshold = default_belief_threshold
        msg = 'Belief threshold argument (belief_threshold) not specified.' + \
              ' Using default belief threshold %.2f' % default_belief_threshold
        logger.info(msg)
    else:
        logger.info('Using belief threshold: %.2f' % belief_threshold)

    twitter_cred = get_twitter_cred(config)
    if twitter_cred:
        logger.info('Using Twitter with given credentials.')
    else:
        logger.info('Not using Twitter due to missing credentials.')

    gmail_cred = get_gmail_cred(config)
    if gmail_cred:
        logger.info('Using Gmail with given credentials.')
    else:
        logger.info('Not using Gmail due to missing credentials.')

    ndex_cred = get_ndex_cred(config)
    if ndex_cred:
        logger.info('Using NDEx with given credentials.')
    else:
        logger.info('Not using NDEx due to missing information.')

    pmids = {}
    # Get email PMIDs
    if gmail_cred:
        logger.info('Getting PMIDs from emails.')
        try:
            email_pmids = get_email_pmids(gmail_cred)
            # Put the email_pmids into the pmids dictionary
            pmids['Gmail'] = email_pmids
            logger.info('Collected %d PMIDs from Gmail', len(email_pmids))
        except Exception:
            logger.exception('Could not get PMIDs from Gmail, continuing.')

    # Get PMIDs for general search_terms and genes
    search_genes = config.get('search_genes')
    search_terms = config.get('search_terms')
    if not search_terms:
        logger.info('No search terms argument (search_terms) specified.')
    else:
        if search_genes is not None:
            search_terms += search_genes
        logger.info('Using search terms: %s' % ', '.join(search_terms))

        if num_days is None:
            num_days = int(config.get('search_terms_num_days', 5))
        logger.info('Searching the last %d days', num_days)

        pmids_term = get_searchterm_pmids(search_terms, num_days=num_days)
        num_pmids = len(set(itt.chain.from_iterable(pmids_term.values())))
        logger.info('Collected %d PMIDs from PubMed search_terms.', num_pmids)
        pmids = _extend_dict(pmids, pmids_term)

    # Get optional grounding map
    gm_path = config.get('grounding_map_path')
    if gm_path:
        try:
            from indra.preassembler.grounding_mapper import load_grounding_map
            grounding_map = load_grounding_map(gm_path)
        except Exception as e:
            logger.error('Could not load grounding map from %s' % gm_path)
            logger.error(e)
            grounding_map = None
    else:
        grounding_map = None

    '''
    # Get PMIDs for search_genes
    # Temporarily removed because Entrez-based article searches
    # are lagging behind and cannot be time-limited
    if not search_genes:
        logger.info('No search genes argument (search_genes) specified.')
    else:
        logger.info('Using search genes: %s' % ', '.join(search_genes))
        pmids_gene = get_searchgenes_pmids(search_genes, num_days=5)
        num_pmids = sum([len(pm) for pm in pmids_gene.values()])
        logger.info('Collected %d PMIDs from PubMed search_genes.' % num_pmids)
        pmids = _extend_dict(pmids, pmids_gene)
    '''
    run_machine(
        model_path,
        pmids,
        belief_threshold,
        search_genes=search_genes,
        ndex_cred=ndex_cred,
        twitter_cred=twitter_cred,
        grounding_map=grounding_map

```
