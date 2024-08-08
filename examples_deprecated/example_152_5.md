# Description
Dump the logs of all jobs with a specified status to files.

# Code
```
import boto3
import re
from datetime import datetime, timezone

s3_path_patt = re.compile('^s3:([-a-zA-Z0-9_]+)/(.*?)$')

class JobLog(object):

def dump_logs(job_queue='run_reach_queue', job_status='RUNNING'):
    """Write logs for all jobs with given the status to files."""
    jobs = get_jobs(job_queue, job_status)
    for job in jobs:
        log = JobLog(job)
        log.get_lines()

```
