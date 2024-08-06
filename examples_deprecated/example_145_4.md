# Description
Gather and merge original grounding information from evidences.

# Code
```
import logging

def merge_groundings(stmts_in):
    """Gather and merge original grounding information from evidences.

    Each Statement's evidences are traversed to find original grounding
    information. These groundings are then merged into an overall consensus
    grounding dict with as much detail as possible.

    The current implementation is only applicable to Statements whose
    concept/agent roles are fixed. Complexes, Associations and Conversions
    cannot be handled correctly.

    Parameters
    ----------
    stmts_in : list[indra.statements.Statement]
        A list of INDRA Statements whose groundings should be merged. These
        Statements are meant to have been preassembled and potentially have
        multiple pieces of evidence.

    Returns
    -------
    stmts_out : list[indra.statements.Statement]
        The list of Statements now with groundings merged at the Statement
        level.
    """
    def surface_grounding(stmt):
        # Find the "best" grounding for a given concept and its evidences
        # and surface that
        for idx, concept in enumerate(stmt.agent_list()):
            if concept is None:
                continue
            aggregate_groundings = {}
            for ev in stmt.evidence:
                if 'agents' in ev.annotations:
                    groundings = ev.annotations['agents']['raw_grounding'][idx]
                    for ns, value in groundings.items():
                        if ns not in aggregate_groundings:
                            aggregate_groundings[ns] = []
                        if isinstance(value, list):
                            aggregate_groundings[ns] += value
                        else:
                            aggregate_groundings[ns].append(value)
            best_groundings = get_best_groundings(aggregate_groundings)
            concept.db_refs = best_groundings

    def get_best_groundings(aggregate_groundings):
        best_groundings = {}
        for ns, values in aggregate_groundings.items():
            # There are 3 possibilities here
            # 1. All the entries in the list are scored in which case we
            # get unique entries and sort them by score
            if all([isinstance(v, (tuple, list)) for v in values]):
                best_groundings[ns] = []
                for unique_value in {v[0] for v in values}:
                    scores = [v[1] for v in values if v[0] == unique_value]
                    best_groundings[ns].append((unique_value, max(scores)))

                best_groundings[ns] = \
                    sorted(best_groundings[ns], key=lambda x: x[1],
                           reverse=True)
            # 2. All the entries in the list are unscored in which case we
            # get the highest frequency entry
            elif all([not isinstance(v, (tuple, list)) for v in values]):
                best_groundings[ns] = max(set(values), key=values.count)
            # 3. There is a mixture, which can happen when some entries were
            # mapped with scores and others had no scores to begin with.
            # In this case, we again pick the highest frequency non-scored
            # entry assuming that the unmapped version is more reliable.
            else:
                unscored_vals = [v for v in values
                                 if not isinstance(v, (tuple, list))]
                best_groundings[ns] = max(set(unscored_vals),
                                          key=unscored_vals.count)
        return best_groundings

    stmts_out = []
    for stmt in stmts_in:
        if not isinstance(stmt, (Complex, Conversion)):
            surface_grounding(stmt)
        stmts_out.append(stmt)

```
