# Description
Updates an existing CX network on NDEx with new CX content.

# Code
```
import io
import time
import ndex2.client
import logging
from indra import get_config


logger = logging.getLogger(__name__)

ndex_base_url = 'http://52.37.175.128'


def get_default_ndex_cred(ndex_cred):
    if ndex_cred:
        username = ndex_cred.get('user')
        password = ndex_cred.get('password')

        if username is not None and password is not None:
            return username, password

    username = get_config('NDEX_USERNAME')
    password = get_config('NDEX_PASSWORD')


def update_network(cx_str, network_id, ndex_cred=None):
    """Update an existing CX network on NDEx with new CX content.

    Parameters
    ----------
    cx_str : str
        String containing the CX content.
    network_id : str
        UUID of the network on NDEx.
    ndex_cred : dict
        A dictionary with the following entries:
        'user': NDEx user name
        'password': NDEx password
    """
    server = 'http://public.ndexbio.org'
    username, password = get_default_ndex_cred(ndex_cred)
    nd = ndex2.client.Ndex2(server, username, password)

    try:
        logger.info('Getting network summary...')
        summary = nd.get_network_summary(network_id)
    except Exception as e:
        logger.error('Could not get NDEx network summary.')
        logger.error(e)
        return

    # Update network content
    try:
        logger.info('Updating network...')
        cx_stream = io.BytesIO(cx_str.encode('utf-8'))
        nd.update_cx_network(cx_stream, network_id)
    except Exception as e:
        logger.error('Could not update NDEx network.')
        logger.error(e)
        return

    # Update network profile
    ver_str = summary.get('version')
    new_ver = _increment_ndex_ver(ver_str)
    profile = {'name': summary.get('name'),
               'description': summary.get('description'),
               'version': new_ver,
               }
    logger.info('Updating NDEx network (%s) profile to %s',
                network_id, profile)

    time.sleep(5)
    profile_retries = 3
    for _ in range(profile_retries):
        try:
            nd.update_network_profile(network_id, profile)
            logger.info('Updated NDEx network profile.')
            break
        except Exception as e:
            logger.error('Could not update NDEx network profile.')
            logger.error(e)
            time.sleep(30)


```
