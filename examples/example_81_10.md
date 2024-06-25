# Description
Test the translation of an inhibition statement to English.

# Code
```
import indra.assemblers.english.assembler as ea

def test_inhibition():
    st = Inhibition(Agent('MEK'), Agent('ERK'))
    s = _stmt_to_text(st)

```
