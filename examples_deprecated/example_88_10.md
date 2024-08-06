# Description
A test for saving statements with unicode text in evidence.

# Code
```
indra.statements import Agent, Phosphorylation, Evidence
indra.util import unicode_strs

def test_save_sentences_unicode():
    mek = Agent('MEK', db_refs={'TEXT': 'MAP2K1'})
    ev = Evidence(source_api='reach', pmid='PMID000asdf',
                  text='foo\U0001F4A9bar')
    st = Phosphorylation(None, mek, evidence=[ev])
    sent = get_sentences_for_agent('MAP2K1', [st])
    assert unicode_strs(sent)
    twg = agent_texts_with_grounding([st])

```
