# Description
Process a paper by calling AWS services to obtain the paper content and process it using ReachProcessor.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import os
import logging
from indra.sources import reach
from indra.literature import pubmed_client, get_full_text, elsevier_client
import datetime
import tzlocal
logger = logging.getLogger(__name__)
try:
	import boto3
	from indra.literature.s3_client import get_reader_json_str, get_full_text
	aws_available = True
except Exception:
	aws_available = False

def process_paper_aws(pmid, start_time_local):
    try:
        metadata, content_type = get_full_text(pmid, metadata=True)
    except Exception as e:
        logger.error('Could not get content from S3: %s' % e)
        return None, None
    logger.info('Downloading %s output from AWS' % pmid)
    reach_json_str = get_reader_json_str('reach', pmid)
    if not reach_json_str:
        logger.info('Could not get output.')
        return None, content_type
    rp = reach.process_json_str(reach_json_str)

    current_time_local = datetime.datetime.now(tzlocal.get_localzone())
    dt_script = current_time_local - start_time_local
    last_mod_remote = metadata['LastModified']
    dt = (current_time_local - last_mod_remote)
    # If it was not modified since the script started
    if dt > dt_script:
        content_type = 'existing_json'

```
