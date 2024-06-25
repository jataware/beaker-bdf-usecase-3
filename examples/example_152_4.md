# Description
Get a list of jobs with their `jobName` and `jobId` for a specified status in an AWS Batch queue.

# Code
```

def get_jobs(job_queue='run_reach_queue', job_status='RUNNING'):
    """Returns a list of dicts with jobName and jobId for each job with the
    given status."""
    batch = boto3.client('batch')
    jobs = batch.list_jobs(jobQueue=job_queue, jobStatus=job_status)

```
