# Description
Test for parsing protein site information using `ProteinSiteInfo`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname

def test_site_text_parser():
    si = ProteinSiteInfo('S10 and S20 residues', None)
    sites = si.get_sites()
    assert len(sites) == 2
    assert sites[0].residue == 'S'
    assert sites[0].position == '10'
    assert sites[1].residue == 'S'

```
