# Description
Map sequences using the SiteMapper.

# Code
```
import logging
from indra.pipeline import register_pipeline

def map_sequence(stmts_in, do_methionine_offset=True,
                 do_orthology_mapping=True, do_isoform_mapping=True, **kwargs):
    """Map sequences using the SiteMapper.

    Parameters
    ----------
    stmts_in : list[indra.statements.Statement]
        A list of statements to map.
    do_methionine_offset : boolean
        Whether to check for off-by-one errors in site position (possibly)
        attributable to site numbering from mature proteins after
        cleavage of the initial methionine. If True, checks the reference
        sequence for a known modification at 1 site position greater
        than the given one; if there exists such a site, creates the
        mapping. Default is True.
    do_orthology_mapping : boolean
        Whether to check sequence positions for known modification sites
        in mouse or rat sequences (based on PhosphoSitePlus data). If a
        mouse/rat site is found that is linked to a site in the human
        reference sequence, a mapping is created. Default is True.
    do_isoform_mapping : boolean
        Whether to check sequence positions for known modifications
        in other human isoforms of the protein (based on PhosphoSitePlus
        data). If a site is found that is linked to a site in the human
        reference sequence, a mapping is created. Default is True.
    use_cache : boolean
        If True, a cache will be created/used from the laction specified by
        SITEMAPPER_CACHE_PATH, defined in your INDRA config or the environment.
        If False, no cache is used. For more details on the cache, see the
        SiteMapper class definition.
    save : Optional[str]
        The name of a pickle file to save the results (stmts_out) into.

    Returns
    -------
    stmts_out : list[indra.statements.Statement]
        A list of mapped statements.
    """
    from indra.preassembler.sitemapper import SiteMapper, default_site_map
    logger.info('Mapping sites on %d statements...' % len(stmts_in))
    sm = SiteMapper(default_site_map,
                    use_cache=kwargs.pop('use_cache', False),
                    do_methionine_offset=do_methionine_offset,
                    do_orthology_mapping=do_orthology_mapping,
                    do_isoform_mapping=do_isoform_mapping)
    valid, mapped = sm.map_sites(stmts_in)
    correctly_mapped_stmts = []
    for ms in mapped:
        correctly_mapped = all([mm.has_mapping() for mm in ms.mapped_mods])
        if correctly_mapped:
            correctly_mapped_stmts.append(ms.mapped_stmt)
    stmts_out = valid + correctly_mapped_stmts
    logger.info('%d statements with valid sites' % len(stmts_out))
    dump_pkl = kwargs.get('save')
    if dump_pkl:
        dump_statements(stmts_out, dump_pkl)
    del sm

```
