# Description
Terminate/cancel all jobs on a specified AWS Batch queue with the option to provide a reason, specify job states, and filter certain jobs.

# Code
```
import boto3
import logging

logger = logging.getLogger(__name__)

def get_ids(job_list):
    if job_list is None:
        return None

def kill_all(job_queue, reason='None given', states=None, kill_list=None):
    """Terminates/cancels all jobs on the specified queue.

    Parameters
    ----------
    job_queue : str
        The name of the Batch job queue on which you wish to terminate/cancel
        jobs.
    reason : str
        Provide a reason for the kill that will be recorded with the job's
        record on AWS.
    states : None or list[str]
        A list of job states to remove. Possible states are 'STARTING',
        'RUNNABLE', and 'RUNNING'. If None, all jobs in all states will be
        ended (modulo the `kill_list` below).
    kill_list : None or list[dict]
        A list of job dictionaries (as returned by the submit function) that
        you specifically wish to kill. All other jobs on the queue will be
        ignored. If None, all jobs on the queue will be ended (modulo the
        above).

    Returns
    -------
    killed_ids : list[str]
        A list of the job ids for jobs that were killed.
    """
    # Default is all states.
    if states is None:
        states = ['STARTING', 'RUNNABLE', 'RUNNING']

    # Get batch client
    batch = boto3.client('batch')

    # Get all other jobs, and terminate them.
    killed_ids = []
    for status in states:
        running = batch.list_jobs(jobQueue=job_queue, jobStatus=status)
        active_job_list = running.get('jobSummaryList')
        if active_job_list is None:
            continue

        for job in active_job_list:
            # Check if this is one of the specified jobs, if any specified.
            ids_to_kill = get_ids(kill_list)
            if ids_to_kill is not None and job['jobId'] not in ids_to_kill:
                continue

            # End the job.
            if status == 'RUNNING':
                logger.info('Terminating {jobName} ({jobId})'.format(**job))
                res = batch.terminate_job(jobId=job['jobId'], reason=reason)
            else:
                logger.info('Canceling {jobName} ({jobId})'.format(**job))
                res = batch.cancel_job(jobId=job['jobId'], reason=reason)

            # Record the result of the kill
            killed_ids.append(res)


```
