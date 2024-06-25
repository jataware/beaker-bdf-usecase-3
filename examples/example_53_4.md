# Description
Test the get_standard_agent function for standardizing agent names and references.

# Code
```
from indra.ontology.standardize import get_standard_agent
from indra.sources.acsn.processor import AcsnProcessor

relations_df = pandas.read_csv(api.ACSN_RELATIONS_URL, sep='\t')
gmt_file = requests.get(api.ACSN_CORRESPONDENCE_URL).text.split('\n')
correspondence_dict = api._transform_gmt(gmt_file)

def test_get_agent():
    # Agents
    VEGFA = get_standard_agent('VEGFA', db_refs={'HGNC': '12680'})
    MIRLET7A = get_standard_agent('MIRLET7A', db_refs={'FPLX': 'MIRLET7A'})

    assert ap.get_agent('VEGFA').db_refs == VEGFA.db_refs, VEGFA.db_refs
    assert ap.get_agent('MIRLET7A*').db_refs == \
           MIRLET7A.db_refs, MIRLET7A.db_refs

```
