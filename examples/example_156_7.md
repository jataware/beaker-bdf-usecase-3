# Description
Method to assemble the CX network from the collected INDRA Statements.

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

    def make_model(self, add_indra_json=True):
        """Assemble the CX network from the collected INDRA Statements.

        This method assembles a CX network from the set of INDRA Statements.
        The assembled network is set as the assembler's cx argument.

        Parameters
        ----------
        add_indra_json : Optional[bool]
            If True, the INDRA Statement JSON annotation is added to each
            edge in the network. Default: True

        Returns
        -------
        cx_str : str
            The json serialized CX model.
        """
        self.add_indra_json = add_indra_json
        for stmt in self.statements:
            if isinstance(stmt, Modification):
                self._add_modification(stmt)
            if isinstance(stmt, SelfModification):
                self._add_self_modification(stmt)
            elif isinstance(stmt, RegulateActivity) or \
                isinstance(stmt, RegulateAmount):
                self._add_regulation(stmt)
            elif isinstance(stmt, Complex):
                self._add_complex(stmt)
            elif isinstance(stmt, Gef):
                self._add_gef(stmt)
            elif isinstance(stmt, Gap):
                self._add_gap(stmt)
            elif isinstance(stmt, Influence):
                self._add_influence(stmt)
        network_description = ''
        self.cx['networkAttributes'].append({'n': 'name',
                                             'v': self.network_name})
        self.cx['networkAttributes'].append({'n': 'description',
                                             'v': network_description})
        cx_str = self.print_cx()

```
