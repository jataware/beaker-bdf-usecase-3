# Description
Submitting a curation for a statement with specific evidence.

# Code
```
from indra.statements import pretty_print_stmts

>> from indra.statements import pretty_print_stmts
>> p = get_statements(agents=["TNF"], ev_limit=3, limit=1)
>> pretty_print_stmts(p.statements)
[LIST INDEX: 0] Activation(TNF(), apoptotic process())
================================================================================
EV INDEX: 0       These published reports in their aggregate support that TNFR2
SOURCE: reach     can lower the threshold of bioavailable TNFalpha needed to
PMID: 19774075    cause apoptosis through TNFR1 thus amplifying extrinsic cell
                  death pathways.
--------------------------------------------------------------------------------
EV INDEX: 1       Our results indicate that IE86 inhibits tumor necrosis factor
SOURCE: reach     (TNF)-alpha induced apoptosis and that the anti-apoptotic
PMID: 19502735    activity of this viral protein correlates with its expression
                  levels.
--------------------------------------------------------------------------------
EV INDEX: 2       This relationship between PUFAs and their anti-inflammatory
SOURCE: reach     metabolites and type 1 DM is supported by the observation that
PMID: 28824543    in a mfat-1 transgenic mouse model whose islets contained
                  increased levels of n-3 PUFAs and significantly lower amounts
                  of n-6 PUFAs compared to the wild type, were resistant to
                  apoptosis induced by TNF-alpha, IL-1beta, and gamma-IFN.
--------------------------------------------------------------------------------
>>
>> submit_curation(p.statements[0].get_hash(), "correct", "usr@bogusemail.com",
>>                 pa_json=p.statements[0].to_json(),
>>                 ev_json=p.statements[0].evidence[1].to_json())

```
