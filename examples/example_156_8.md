# Description
Method to return the assembled CX network as a JSON string.

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

    def print_cx(self, pretty=True):
        """Return the assembled CX network as a json string.

        Parameters
        ----------
        pretty : bool
            If True, the CX string is formatted with indentation (for human
            viewing) otherwise no indentation is used.

        Returns
        -------
        json_str : str
            A json formatted string representation of the CX network.
        """
        def _get_aspect_metadata(aspect):
            count = len(self.cx.get(aspect)) if self.cx.get(aspect) else 0
            if not count:
                return None
            data = {'name': aspect,
                    'idCounter': self._id_counter,
                    'consistencyGroup': 1,
                    'elementCount': count}
            return data
        full_cx = OrderedDict()
        full_cx['numberVerification'] = [{'longNumber': 281474976710655}]
        aspects = ['nodes', 'edges', 'supports', 'citations', 'edgeAttributes',
                   'edgeCitations', 'edgeSupports', 'networkAttributes',
                   'nodeAttributes', 'cartesianLayout']
        full_cx['metaData'] = []
        for aspect in aspects:
            metadata = _get_aspect_metadata(aspect)
            if metadata:
                full_cx['metaData'].append(metadata)
        for k, v in self.cx.items():
            full_cx[k] = v
        full_cx['status'] = [{'error': '', 'success': True}]
        full_cx = [{k: v} for k, v in full_cx.items()]
        if pretty:
            json_str = json.dumps(full_cx, indent=2)
        else:
            json_str = json.dumps(full_cx)

```
