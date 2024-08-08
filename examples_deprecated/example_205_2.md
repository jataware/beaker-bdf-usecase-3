# Description
Get all PTMs (Post-Translational Modifications) from OmniPath in JSON format.

# Code
```
import requests


def _get_modifications():
    """Get all PTMs from Omnipath in JSON format.

    Returns
    -------
    JSON content for PTMs.
    """
    params = {'format': 'json',
              'fields': ['curation_effort', 'isoforms', 'references',
                         'resources', 'sources']}
    ptm_url = '%s/ptms' % op_url
    res = requests.get(ptm_url, params=params)
    if not res.status_code == 200 or not res.text:
        return None
    else:

```
