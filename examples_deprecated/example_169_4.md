# Description
Sample paths from an influence map using Paths Graph library.

# Code
```
networkx as nx
collections import Counter
numpy as np

    def _sample_paths(self, input_rule_set, obs_name, target_polarity,
                      max_paths=1, max_path_length=5):
        if max_paths == 0:
            raise ValueError("max_paths cannot be 0 for path sampling.")
        if not has_pg:
            raise ImportError("Paths Graph is not imported")
        # Convert path polarity representation from 0/1 to 1/-1

        def convert_polarities(path_list):
            return [tuple((n[0], 0 if n[1] > 0 else 1) for n in path)
                    for path in path_list]

        pg_polarity = 0 if target_polarity > 0 else 1
        nx_graph = self._im_to_signed_digraph(self.get_im())
        # Add edges from dummy node to input rules
        source_node = 'SOURCE_NODE'
        for rule in input_rule_set:
            nx_graph.add_edge(source_node, rule, sign=0)
        # -------------------------------------------------
        # Create combined paths_graph
        f_level, b_level = pg.get_reachable_sets(nx_graph, source_node,
                                                 obs_name, max_path_length,
                                                 signed=True)
        pg_list = []
        for path_length in range(1, max_path_length+1):
            cfpg = pg.CFPG.from_graph(
                    nx_graph, source_node, obs_name, path_length, f_level,
                    b_level, signed=True, target_polarity=pg_polarity)
            pg_list.append(cfpg)
        combined_pg = pg.CombinedCFPG(pg_list)
        # Make sure the combined paths graph is not empty
        if not combined_pg.graph:
            pr = PathResult(
                False, 'NO_PATHS_FOUND', max_paths, max_path_length)
            pr.path_metrics = None
            pr.paths = []
            return pr

        # Get a dict of rule objects
        rule_obj_dict = {}
        for ann in self.model.annotations:
            if ann.predicate == 'rule_has_object':
                rule_obj_dict[ann.subject] = ann.object

        # Get monomer initial conditions
        ic_dict = {}
        for mon in self.model.monomers:
            # FIXME: A hack that depends on the _0 convention
            ic_name = '%s_0' % mon.name
            # TODO: Wrap this in try/except?
            ic_param = self.model.parameters[ic_name]
            ic_value = ic_param.value
            ic_dict[mon.name] = ic_value

        # Set weights in PG based on model initial conditions
        for cur_node in combined_pg.graph.nodes():
            edge_weights = {}
            rule_obj_list = []
            edge_weights_by_gene = {}
            for u, v in combined_pg.graph.out_edges(cur_node):
                v_rule = v[1][0]
                # Get the object of the rule (a monomer name)
                rule_obj = rule_obj_dict.get(v_rule)
                if rule_obj:
                    # Add to list so we can count instances by gene
                    rule_obj_list.append(rule_obj)
                    # Get the abundance of rule object from the initial
                    # conditions
                    # TODO: Wrap in try/except?
                    ic_value = ic_dict[rule_obj]
                else:
                    ic_value = 1.0
                edge_weights[(u, v)] = ic_value
                edge_weights_by_gene[rule_obj] = ic_value
            # Get frequency of different rule objects
            rule_obj_ctr = Counter(rule_obj_list)
            # Normalize results by weight sum and gene frequency at this level
            edge_weight_sum = sum(edge_weights_by_gene.values())
            edge_weights_norm = {}
            for e, v in edge_weights.items():
                v_rule = e[1][1][0]
                rule_obj = rule_obj_dict.get(v_rule)
                if rule_obj:
                    rule_obj_count = rule_obj_ctr[rule_obj]
                else:
                    rule_obj_count = 1
                edge_weights_norm[e] = ((v / float(edge_weight_sum)) /
                                        float(rule_obj_count))
            # Add edge weights to paths graph
            nx.set_edge_attributes(combined_pg.graph, name='weight',
                                   values=edge_weights_norm)

        # Sample from the combined CFPG
        paths = combined_pg.sample_paths(max_paths)
        # -------------------------------------------------
        if paths:
            pr = PathResult(True, 'PATHS_FOUND', max_paths, max_path_length)
            pr.path_metrics = None
            # Convert path polarity representation from 0/1 to 1/-1
            pr.paths = convert_polarities(paths)
            # Strip off the SOURCE_NODE prefix
            pr.paths = [p[1:] for p in pr.paths]
        else:
            assert False
            pr = PathResult(
                False, 'NO_PATHS_FOUND', max_paths, max_path_length)
            pr.path_metrics = None
            pr.paths = []

```
