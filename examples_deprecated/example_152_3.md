# Description
Apply tags to the current EC2 instance when running INDRA in an EC2 instance.

# Code
```
import boto3
import logging
import requests

logger = logging.getLogger(__name__)

def tag_instance(instance_id, **tags):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    tag_list = [{'Key': k, 'Value': v} for k, v in tags.items() if k and v]
    if tag_list:
        instance.create_tags(Tags=tag_list)
        vols = instance.volumes.all()
        for page in vols.pages():
            for vol in page:
                vol.create_tags(Tags=tag_list)

def tag_myself(project='aske', **other_tags):
    """Function run when indra is used in an EC2 instance to apply tags."""
    base_url = "http://169.254.169.254"
    try:
        resp = requests.get(base_url + "/latest/meta-data/instance-id")
    except requests.exceptions.ConnectionError:
        logger.warning("Could not connect to service. Note this should only "
                       "be run from within a batch job.")
        return
    instance_id = resp.text
    tag_instance(instance_id, project=project, **other_tags)

```
