# Description
Process all annotations that have been written in BEL

# Code
```
import logging
import requests
from indra.config import get_config
from .processor import HypothesisProcessor
from .annotator import statement_to_annotations

logger = logging.getLogger(__name__)

base_url = 'https://api.hypothes.is/api/'
api_key = get_config('HYPOTHESIS_API_KEY')
headers = {'Authorization': 'Bearer %s' % api_key,
           'Accept': 'application/vnd.hypothesis.v1+json',
           'content-type': 'application/json'}
indra_group = get_config('HYPOTHESIS_GROUP')

... # other function definitions like send_get_request, send_post_request, etc.


        from indra.sources import hypothesis
        processor = hypothesis.process_annotations(group='Z8RNqokY', reader='bel')
        processor.statements
        # returns: [Phosphorylation(AKT(), PCGF2(), T, 334)]

    If this example doesn't work, try joining the group with this link:

```
