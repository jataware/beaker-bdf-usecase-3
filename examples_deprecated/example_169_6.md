# Description
Prune influence map by removing edges between rules that cause problematic non-transitivity.

# Code
```

    def prune_influence_map(self):
        """Remove edges between rules causing problematic non-transitivity.

        First, all self-loops are removed. After this initial step, edges are
        removed between rules when they share *all* child nodes except for each
        other; that is, they have a mutual relationship with each other and
        share all of the same children.

        Note that edges must be removed in batch at the end to prevent edge
        removal from affecting the lists of rule children during the comparison
        process.
        """
        im = self.get_im()

        # First, remove all self-loops
        logger.info('Removing self loops')
        edges_to_remove = []
        for e in im.edges():
            if e[0] == e[1]:
                logger.info('Removing self loop: %s', e)
                edges_to_remove.append((e[0], e[1]))
        # Now remove all the edges to be removed with a single call
        im.remove_edges_from(edges_to_remove)

        # Remove parameter nodes from influence map
        remove_im_params(self.model, im)

        # Now compare nodes pairwise and look for overlap between child nodes
        logger.info('Get successors of each node')
        succ_dict = {}
        for node in im.nodes():
            succ_dict[node] = set(im.successors(node))
        # Sort and then group nodes by number of successors
        logger.info('Compare combinations of successors')
        group_key_fun = lambda x: len(succ_dict[x])
        nodes_sorted = sorted(im.nodes(), key=group_key_fun)
        groups = itertools.groupby(nodes_sorted, key=group_key_fun)
        # Now iterate over each group and then construct combinations
        # within the group to check for shared sucessors
        edges_to_remove = []
        for gix, group in groups:
            combos = itertools.combinations(group, 2)
            for ix, (p1, p2) in enumerate(combos):
                # Children are identical except for mutual relationship
                if succ_dict[p1].difference(succ_dict[p2]) == set([p2]) and \
                   succ_dict[p2].difference(succ_dict[p1]) == set([p1]):
                    for u, v in ((p1, p2), (p2, p1)):
                        edges_to_remove.append((u, v))
                        logger.debug('Will remove edge (%s, %s)', u, v)
        logger.info('Removing %d edges from influence map' %
                    len(edges_to_remove))
        # Now remove all the edges to be removed with a single call

```
