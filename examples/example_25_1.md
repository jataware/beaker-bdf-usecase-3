# Description
Update JSON data by looking up the ontology through PyOBO using `PyOboClient.update_by_prefix`.

# Code
```
import json
import logging
import os
import pathlib
import pickle
import re
from collections import defaultdict
from operator import attrgetter
from typing import Callable, List, Mapping, Optional
import pyobo
from indra.resources import get_resource_path

logger = logging.getLogger(__name__)

def _get_pyobo_rels(term, *, include_relations=False):
    rv = defaultdict(list)
    for parent in term.parents:
        rv["is_a"].append(parent.identifier)
    if include_relations:
        for type_def, references in term.relationships.items():
            for reference in references:
                rv[type_def.curie].append(reference.curie)
    return dict(rv)


 def prune_standard(entries):
     return prune_empty_entries(entries, {'synonyms', 'xrefs', 'alt_ids', 'relations'})


def prune_empty_entries(entries, keys):
    for entry in entries:
        for key in keys:
            if key in entry and not entry[key]:
                entry.pop(key)

    @classmethod
    def update_by_prefix(
        cls,
        prefix: str,
        include_relations: bool = False,
        predicate: Optional[Callable[["pyobo.Term"], bool]] = None,
        indra_prefix: str = None,
    ):
        """Update the JSON data by looking up the ontology through PyOBO."""
        import pyobo

        terms = iter(pyobo.get_ontology(prefix))
        if predicate:
            terms = filter(predicate, terms)
        terms = sorted(terms, key=attrgetter("identifier"))
        entries = [
            {
                'id': term.identifier,
                'name': term.name,
                # Synonyms can be duplicated in OBO due to different provenance
                # so we deduplicate here
                'synonyms': sorted({synonym.name for synonym in term.synonyms},
                                   key=lambda x: x.casefold()),
                'xrefs': [
                    dict(namespace=xref.prefix, id=xref.identifier)
                    for xref in term.xrefs
                ],
                'alt_ids': sorted([
                    alt_id.identifier
                    for alt_id in term.alt_ids
                ]),
                'relations': _get_pyobo_rels(
                    term,
                    include_relations=include_relations,
                ),
            }
            for term in terms
        ]
        entries = prune_standard(entries)
        indra_prefix = prefix if not indra_prefix else indra_prefix
        resource_path = get_resource_path(f'{indra_prefix}.json')
        with open(resource_path, 'w') as file:

```
