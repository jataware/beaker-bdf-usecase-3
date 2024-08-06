# Description
Method to set protein expression data and mutational status as node attributes.

# Code
```
import logging

logger = logging.getLogger(__name__)

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

    def set_context(self, cell_type):
        """Set protein expression data and mutational status as node attribute

        This method uses :py:mod:`indra.databases.context_client` to get
        protein expression levels and mutational status for a given cell type
        and set a node attribute for proteins accordingly.

        Parameters
        ----------
        cell_type : str
            Cell type name for which expression levels are queried.
            The cell type name follows the CCLE database conventions.
            Example: LOXIMVI_SKIN, BT20_BREAST
        """
        node_names = [node['n'] for node in self.cx['nodes']]
        res_expr = context_client.get_protein_expression(node_names,
                                                         [cell_type])
        res_mut = context_client.get_mutations(node_names,
                                               [cell_type])
        res_expr = res_expr.get(cell_type)
        res_mut = res_mut.get(cell_type)
        if not res_expr:
            msg = 'Could not get protein expression for %s cell type.' % \
                  cell_type
            logger.warning(msg)

        if not res_mut:
            msg = 'Could not get mutational status for %s cell type.' % \
                  cell_type
            logger.warning(msg)

        if not res_expr and not res_mut:
            return

        self.cx['networkAttributes'].append({'n': 'cellular_context',
                                             'v': cell_type})
        counter = 0
        for node in self.cx['nodes']:
            amount = res_expr.get(node['n'])
            mut = res_mut.get(node['n'])
            if amount is not None:
                node_attribute = {'po': node['@id'],
                                  'n': 'expression_amount',
                                  'v': int(amount)}
                self.cx['nodeAttributes'].append(node_attribute)
            if mut is not None:
                is_mutated = 1 if mut else 0
                node_attribute = {'po': node['@id'],
                                  'n': 'is_mutated',
                                  'v': is_mutated}
                self.cx['nodeAttributes'].append(node_attribute)
            if mut is not None or amount is not None:
                counter += 1

```
