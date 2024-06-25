# Description
Sets the style of the network to a given template network's style.

# Code
```
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


def set_style(network_id, ndex_cred=None, template_id=None):
    """Set the style of the network to a given template network's style

    Parameters
    ----------
    network_id : str
        The UUID of the NDEx network whose style is to be changed.
    ndex_cred : dict
        A dictionary of NDEx credentials.
    template_id : Optional[str]
        The UUID of the NDEx network whose style is used on the
        network specified in the first argument.
    """
    if not template_id:
        template_id = "ea4ea3b7-6903-11e7-961c-0ac135e8bacf"
    logger.info('Setting network style based on template: %s' %
                template_id)
    server = 'http://public.ndexbio.org'
    username, password = get_default_ndex_cred(ndex_cred)

    retries = 3
    for _ in range(retries):
        try:
            time.sleep(5)
            source_network = ndex2.create_nice_cx_from_server(
                username=username, password=password, uuid=network_id,
                server=server)
            source_network.apply_template(server, template_id)
            source_network.update_to(network_id, server=server,
                                     username=username, password=password)
            logger.info('Set network style.')
            break
        except Exception as e:
            logger.error('Could not set style of NDEx network.')

```
