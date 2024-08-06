# Description
Method to create a new NDEx network of the assembled CX model.

# Code
```
class CxAssembler(object):
    def __init__(self, stmts=None, network_name=None):
        if stmts is None:
            self.statements = []
        else:
            self.statements = stmts
        if network_name is None:
            self.network_name = 'indra_assembled'
        else:
            self.network_name = network_name
        self.cx = {'nodes': [], 'edges': [], 'nodeAttributes': [], 'edgeAttributes': [], 'citations': [], 'edgeCitations': [], 'supports': [], 'edgeSupports': [], 'networkAttributes': []}
        self._existing_nodes = {}
        self._existing_edges = {}

    def upload_model(self, ndex_cred=None, private=True, style='default'):
        """Creates a new NDEx network of the assembled CX model.

        To upload the assembled CX model to NDEx, you need to have
        a registered account on NDEx (http://ndexbio.org/) and have
        the `ndex` python package installed. The uploaded network
        is private by default.

        Parameters
        ----------
        ndex_cred : Optional[dict]
            A dictionary with the following entries:
            'user': NDEx user name
            'password': NDEx password
        private : Optional[bool]
            Whether or not the created network will be private on NDEX.
        style : Optional[str]
            This optional parameter can either be (1)
            The UUID of an existing NDEx network whose style should be applied
            to the new network. (2) Unspecified or 'default' to use
            the default INDRA-assembled network style. (3) None to
            not set a network style.

        Returns
        -------
        network_id : str
            The UUID of the NDEx network that was created by uploading
            the assembled CX model.
        """
        cx_str = self.print_cx()
        if not ndex_cred:
            username, password = ndex_client.get_default_ndex_cred({})
            ndex_cred = {'user': username,
                         'password': password}
        network_id = ndex_client.create_network(cx_str, ndex_cred, private)
        if network_id and style:
            template_id = None if style == 'default' else style
            nretries = 3
            for retry_idx in range(nretries):
                time.sleep(3)
                try:
                    ndex_client.set_style(network_id, ndex_cred, template_id)
                    break
                except Exception:
                    msg = 'Style setting failed, '
                    if retry_idx + 1 < nretries:
                        logger.info(msg + 'retrying %d more times' %
                                    (nretries - (retry_idx+1)))
                    else:
                        logger.info(msg + 'the network will be missing style '
                                    'information.')

```
