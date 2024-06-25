# Description
Testing fallback mechanism when getting agent name using 'get_agent_from_grounding' with and without web fallback.

# Code
```

def test_name_web_fallback():
    ag = get_agent_from_grounding('uniprotkb:Q174W8', up_web_fallback=False)
    assert ag.name == 'Q174W8'
    ag = get_agent_from_grounding('uniprotkb:Q174W8', up_web_fallback=True)

```
