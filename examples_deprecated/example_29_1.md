# Description
Getting collection publications from bioRxiv/medRxiv collections using a specified date cutoff.

# Code
```
import requests
import datetime


def get_collection_pubs(collection_id, min_date=None):
    """Get list of DOIs from a biorxiv/medrxiv collection.

    Parameters
    ----------
    collection_id : str
        The identifier of the collection to fetch.
    min_date : Optional[datetime.datetime]
        A datetime object representing an cutoff. If given, only
        publications that were released on or after the given date
        are returned. By default, no date constraint is applied.

    Returns
    -------
    list of dict
        A list of the publication entries which include the abstract and other
        metadata.
    """
    res = requests.get(collection_url + collection_id)
    res.raise_for_status()
    pubs = res.json()['rels']
    if min_date:
        new_rels = []
        for pub in pubs:
            try:
                date = datetime.datetime.strptime(pub.get('rel_date'),
                                                  '%Y-%m-%d')
            except Exception:
                continue
            if date >= min_date:
                new_rels.append(pub)
        return new_rels

```
