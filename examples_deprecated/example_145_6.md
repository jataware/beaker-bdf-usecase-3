# Description
Run preassembly on a list of statements.

# Code
```
import logging
from indra.pipeline import register_pipeline
from indra.belief import BeliefEngine
from indra.preassembler import Preassembler, flatten_evidence

@register_pipeline
def run_preassembly(stmts_in, return_toplevel=True, poolsize=None,
                    size_cutoff=None, belief_scorer=None, ontology=None,
                    matches_fun=None, refinement_fun=None,
                    flatten_evidence=False, flatten_evidence_collect_from=None,
                    normalize_equivalences=False, normalize_opposites=False,
                    normalize_ns='WM', run_refinement=True, filters=None,
                    **kwargs):
    """Run preassembly on a list of statements.

    Parameters
    ----------
    stmts_in : list[indra.statements.Statement]
        A list of statements to preassemble.
    return_toplevel : Optional[bool]
        If True, only the top-level statements are returned. If False,
        all statements are returned irrespective of level of specificity.
        Default: True
    poolsize : Optional[int]
        The number of worker processes to use to parallelize the
        comparisons performed by the function. If None (default), no
        parallelization is performed. NOTE: Parallelization is only
        available on Python 3.4 and above.
    size_cutoff : Optional[int]
        Groups with size_cutoff or more statements are sent to worker
        processes, while smaller groups are compared in the parent process.
        Default value is 100. Not relevant when parallelization is not
        used.
    belief_scorer : Optional[indra.belief.BeliefScorer]
        Instance of BeliefScorer class to use in calculating Statement
        probabilities. If None is provided (default), then the default
        scorer is used.
    ontology : Optional[IndraOntology]
        IndraOntology object to use for preassembly
    matches_fun : Optional[function]
        A function to override the built-in matches_key function of statements.
    refinement_fun : Optional[function]
        A function to override the built-in refinement_of function of
        statements.
    flatten_evidence : Optional[bool]
        If True, evidences are collected and flattened via supports/supported_by
        links. Default: False
    flatten_evidence_collect_from : Optional[str]
        String indicating whether to collect and flatten evidence from the
        `supports` attribute of each statement or the `supported_by` attribute.
        If not set, defaults to 'supported_by'.
        Only relevant when flatten_evidence is True.
    normalize_equivalences : Optional[bool]
        If True, equivalent groundings are rewritten to a single standard one.
        Default: False
    normalize_opposites : Optional[bool]
        If True, groundings that have opposites in the ontology are rewritten
        to a single standard one.
    normalize_ns : Optional[str]
        The name space with respect to which equivalences and opposites are
        normalized.
    filters : Optional[list[:py:class:indra.preassembler.refinement.RefinementFilter]]
        A list of RefinementFilter classes that implement filters on
        possible statement refinements. For details on how to
        construct such a filter, see the documentation of
        :py:class:`indra.preassembler.refinement.RefinementFilter`.
        If no user-supplied filters are provided, the default ontology-based
        filter is applied. If a list of filters is provided here, the
        :py:class:`indra.preassembler.refinement.OntologyRefinementFilter`
        isn't appended by default, and should be added by the user, if
        necessary. Default: None
    save : Optional[str]
        The name of a pickle file to save the results (stmts_out) into.
    save_unique : Optional[str]
        The name of a pickle file to save the unique statements into.

    Returns
    -------
    stmts_out : list[indra.statements.Statement]
        A list of preassembled top-level statements.
    """
    dump_pkl_unique = kwargs.get('save_unique')
    use_ontology = ontology if ontology is not None else bio_ontology
    be = BeliefEngine(scorer=belief_scorer, matches_fun=matches_fun)
    pa = Preassembler(use_ontology, stmts_in, matches_fun=matches_fun,
                      refinement_fun=refinement_fun)
    if normalize_equivalences:
        logger.info('Normalizing equals on %d statements' % len(pa.stmts))
        pa.normalize_equivalences(normalize_ns)
    if normalize_opposites:
        logger.info('Normalizing opposites on %d statements' % len(pa.stmts))
        pa.normalize_opposites(normalize_ns)

    dedupl_stmts = run_preassembly_duplicate(pa, be, save=dump_pkl_unique)
    if not run_refinement:
        return dedupl_stmts

    dump_pkl = kwargs.get('save')
    size_cutoff = size_cutoff if size_cutoff else 100
    if not flatten_evidence_collect_from:
        flatten_evidence_collect_from = 'supported_by'
    options = {'save': dump_pkl, 'return_toplevel': return_toplevel,
               'poolsize': poolsize, 'size_cutoff': size_cutoff,
               'flatten_evidence': flatten_evidence,
               'flatten_evidence_collect_from': flatten_evidence_collect_from,
               'filters': filters
               }
    stmts_out = run_preassembly_related(pa, be, **options)

```
