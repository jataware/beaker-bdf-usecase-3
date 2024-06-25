# Description
Test embedding of monomer pattern (mp)

# Code
```
pysb import Monomer
indra.explanation.model_checker.pysb import _mp_embeds_into

@with_model
def test_mp_embedding():
    # Create a PySB model
    Monomer('A', ['b', 'other'], {'other':['u','p']})
    mp1 = A(other='u')
    mp2 = A()
    mp3 = A(other='p')
    assert _mp_embeds_into(mp1, mp2)
    assert not _mp_embeds_into(mp2, mp1)
    assert _mp_embeds_into(mp3, mp2)
    assert not _mp_embeds_into(mp2, mp3)
    assert not _mp_embeds_into(mp3, mp1)

```
