# Description
Prune positive edges between X degrading and X forming a complex with Y.

# Code
```

def prune_influence_map_degrade_bind_positive(self, model_stmts):
    """Prune positive edges between X degrading and X forming a
    complex with Y."""
    im = self.get_im()
    edges_to_prune = []
    for r1, r2, data in im.edges(data=True):
        s1 = stmt_from_rule(r1, self.model, model_stmts)
        s2 = stmt_from_rule(r2, self.model, model_stmts)
        # Make sure this is a degradation/binding combo
        s1_is_degrad = (s1 and isinstance(s1, DecreaseAmount))
        s2_is_bind = (s2 and isinstance(s2, Complex) and 'bind' in r2)
        if not s1_is_degrad or not s2_is_bind:
            continue
        # Make sure what is degraded is part of the complex
        if s1.obj.name not in [m.name for m in s2.members]:
            continue
        # Make sure we're dealing with a positive influence
        if data['sign'] == 1:
            edges_to_prune.append((r1, r2))
    logger.info('Removing %d edges from influence map' %
                len(edges_to_prune))

```
