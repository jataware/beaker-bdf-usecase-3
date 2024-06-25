# Description
Tag a specific EC2 instance with provided tags.

# Code
```
import boto3
import logging


def tag_instance(instance_id, **tags):
    """Tag a single ec2 instance."""
    logger.debug("Got request to add tags %s to instance %s."
                 % (str(tags), instance_id))
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)

    # Remove None's from `tags` and reformat to the list format that
    # boto3 expects
    tag_list = [{'Key': k, 'Value': v} for k, v in tags.items() if k and v]
    if tag_list:
        logger.info('Adding project tags "%s" to instance %s'
                    % (str(tag_list), instance_id))
        instance.create_tags(Tags=tag_list)
        vols = instance.volumes.all()
        for page in vols.pages():
            for vol in page:
                vol.create_tags(Tags=tag_list)
    else:
        logger.info('No new tags from: %s' % str(tags))
    instance_tags = {tag.get('Key'): tag.get('Value') for tag in instance.tags}
    logger.info('Updated instance tags: %s' % instance_tags)

```
