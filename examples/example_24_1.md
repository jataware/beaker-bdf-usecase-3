# Description
Creates a new NDEx network of the assembled CX model and uploads it to NDEx.

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


def create_network(cx_str, ndex_cred=None, private=True):
    """Creates a new NDEx network of the assembled CX model.

    To upload the assembled CX model to NDEx, you need to have
    a registered account on NDEx (http://ndexbio.org/) and have
    the `ndex` python package installed. The uploaded network
    is private by default.

    Parameters
    ----------
    ndex_cred : dict
        A dictionary with the following entries:
        'user': NDEx user name
        'password': NDEx password

    Returns
    -------
    network_id :  str
        The UUID of the NDEx network that was created by uploading
        the assembled CX model.
    """
    username, password = get_default_ndex_cred(ndex_cred)
    nd = ndex2.client.Ndex2('http://public.ndexbio.org',
                            username=username,
                            password=password)
    cx_stream = io.BytesIO(cx_str.encode('utf-8'))
    try:
        logger.info('Uploading network to NDEx.')
        network_uri = nd.save_cx_stream_as_new_network(cx_stream)
    except Exception as e:
        logger.error('Could not upload network to NDEx.')
        logger.error(e)
        return

    network_id = network_uri.rsplit('/')[-1]

    # Set the network to public. This often fails due to time-out issues,
    # therefore we implement a wait and retry approach here.
    if not private:
        nretries = 3
        for retry_idx in range(nretries):
            time.sleep(3)
            try:
                logger.info('Making network public.')
                nd.make_network_public(network_id)
                break
            except Exception:
                msg = 'Setting network to public failed, '
                if retry_idx + 1 < nretries:
                    logger.info(msg + 'retrying %d more times.' %
                                (nretries - (retry_idx + 1)))
                else:
                    logger.info(msg + 'the network will remain private.')

    logger.info('The UUID for the uploaded network is: %s' % network_id)
    logger.info('View at: http://ndexbio.org/#/network/%s' % network_id)

```
