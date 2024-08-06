# Description
Wrapper for calling the OmniPath interactions API to fetch interaction data based on provided datasets.

# Code
```
import requests


def _get_interactions(datasets=None):
    """Wrapper for calling the omnipath interactions API

    See full list of query options here:
    https://omnipathdb.org/queries/interactions

    Parameters
    ----------
    datasets
        A list of dataset names. Options are:
            dorothea, kinaseextra, ligrecextra, lncrna_mrna, mirnatarget,
            omnipath, pathwayextra, tf_mirna, tf_target, tfregulons
        Default: 'ligrecextra'

    Returns
    -------
    dict
        json of database request
    """
    interactions_url = '%s/interactions' % op_url
    params = {
        'fields': ['curation_effort', 'entity_type', 'references',
                   'resources', 'sources', 'type'],
        'format': 'json',
        'datasets': datasets or ['ligrecextra']
    }
    res = requests.get(interactions_url, params=params)
    res.raise_for_status()


```
