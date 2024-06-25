# Description
Test embedding of complex pattern (cp)

# Code
```
pysb import Monomer
indra.explanation.model_checker.pysb import _cp_embeds_into

@with_model
def test_cp_embedding():
    Monomer('A', ['b', 'other'], {'other': ['u','p']})
    Monomer('B', ['b'])
    cp1 = A(b=1, other='p') % B(b=1)
    cp2 = A()
    cp3 = A(b=1, other='u') % B(b=1)
    cp4 = A(other='p')
    cp5 = A(b=1) % B(b=1)
    # FIXME Some tests not performed because ComplexPatterns for second term
    # FIXME are not yet supported
    assert _cp_embeds_into(cp1, cp2)
    #assert not _cp_embeds_into(cp1, cp3)
    assert _cp_embeds_into(cp1, cp4)
    #assert not _cp_embeds_into(cp1, cp5)
    #assert not _cp_embeds_into(cp2, cp1)
    #assert not _cp_embeds_into(cp2, cp3)
    assert not _cp_embeds_into(cp2, cp4)
    #assert not _cp_embeds_into(cp2, cp5)
    #assert not _cp_embeds_into(cp3, cp1)
    assert _cp_embeds_into(cp3, cp2)
    assert not _cp_embeds_into(cp3, cp4)
    #assert _cp_embeds_into(cp3, cp5)
    #assert not _cp_embeds_into(cp4, cp1)
    assert _cp_embeds_into(cp4, cp2)
    #assert not _cp_embeds_into(cp4, cp3)
    #assert not _cp_embeds_into(cp4, cp5)
    #assert not _cp_embeds_into(cp5, cp1)
    assert _cp_embeds_into(cp5, cp2)
    #assert not _cp_embeds_into(cp5, cp3)

```
