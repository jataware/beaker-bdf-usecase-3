# Description
Set context of all nodes and node members from CCLE.

# Code
```
import json
import logging
import itertools
import collections
import numpy as np
from copy import deepcopy
from indra.statements import *
from indra.databases import context_client, get_identifiers_url
from indra.tools.expand_families import Expander
from indra.ontology.bio import bio_ontology
from indra.ontology.standardize import standardize_db_refs

expander = Expander(ontology=bio_ontology)

logger = logging.getLogger(__name__)

class CyJSAssembler(object):
    def __init__(self, stmts=None):
        if not stmts:
            self.statements = []
        else:
            self.statements = stmts
        self._edges = []
        self._nodes = []
        self._existing_nodes = {}
        self._id_counter = 0
        self._exp_colorscale = []
        self._mut_colorscale = []
        self._gene_names = []
        self._context = {}

    def get_gene_names(self):
        gene_names = []
        for node in self._nodes:
            members = node['data'].get('members')
            if members:
                gene_names += list(members.keys())
            else:
                if node['data']['name'].startswith('Group'):
                    continue
                gene_names.append(node['data']['name'])

    def set_CCLE_context(self, cell_types):
        """Set context of all nodes and node members from CCLE."""
        self.get_gene_names()

        # Get expression and mutations from context client
        exp_values = \
            context_client.get_protein_expression(self._gene_names, cell_types)
        mut_values = \
            context_client.get_mutations(self._gene_names, cell_types)

        # Make a dict of presence/absence of mutations
        muts = {cell_line: {} for cell_line in cell_types}
        for cell_line, entries in mut_values.items():
            if entries is not None:
                for gene, mutations in entries.items():
                    if mutations:
                        muts[cell_line][gene] = 1
                    else:
                        muts[cell_line][gene] = 0

        # Create bins for the exp values
        # because colorbrewer only does 3-9 bins and I don't feel like
        # reinventing color scheme theory, this will only bin 3-9 bins
        def bin_exp(expression_dict):
            d = expression_dict
            exp_values = []
            for line in d:
                for gene in d[line]:
                    val = d[line][gene]
                    if val is not None:
                        exp_values.append(val)
            thr_dict = {}
            for n_bins in range(3, 10):
                bin_thr = np.histogram(np.log10(exp_values), n_bins)[1][1:]
                thr_dict[n_bins] = bin_thr
            # this dict isn't yet binned, that happens in the loop
            binned_dict = {x: deepcopy(expression_dict) for x in range(3, 10)}
            for n_bins in binned_dict:
                for line in binned_dict[n_bins]:
                    for gene in binned_dict[n_bins][line]:
                        # last bin is reserved for None
                        if binned_dict[n_bins][line][gene] is None:
                            binned_dict[n_bins][line][gene] = n_bins
                        else:
                            val = np.log10(binned_dict[n_bins][line][gene])
                            for thr_idx, thr in enumerate(thr_dict[n_bins]):
                                if val <= thr:
                                    binned_dict[n_bins][line][gene] = thr_idx
                                    break
            return binned_dict
        binned_exp = bin_exp(exp_values)

        context = {'bin_expression': binned_exp,
                   'mutation': muts}

```
