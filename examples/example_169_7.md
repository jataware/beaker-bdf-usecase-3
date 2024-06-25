# Description
Prune influence map to include only edges where the object of the upstream rule matches the subject of the downstream rule.

# Code
```

def prune_influence_map_subj_obj(self):
    """Prune influence map to include only edges where the object of the
    upstream rule matches the subject of the downstream rule."""
    def get_rule_info(r):
        result = {}
        for ann in self.model.annotations:
            if ann.subject == r:
                if ann.predicate == 'rule_has_subject':
                    result['subject'] = ann.object
                elif ann.predicate == 'rule_has_object':
                    result['object'] = ann.object
        return result
    im = self.get_im()
    rules = im.nodes()
    edges_to_prune = []
    for r1, r2 in itertools.permutations(rules, 2):
        if (r1, r2) not in im.edges():
            continue
        r1_info = get_rule_info(r1)
        r2_info = get_rule_info(r2)
        if 'object' not in r1_info or 'subject' not in r2_info:
            continue
        if r1_info['object'] != r2_info['subject']:
            logger.info("Removing edge %s --> %s" % (r1, r2))
            edges_to_prune.append((r1, r2))
    logger.info('Removing %d edges from influence map' %
                len(edges_to_prune))

```
