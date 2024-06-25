# Description
Extracting clean text from raw rxiv XML content.

# Code
```

def get_text_from_rxiv_xml(rxiv_xml):
    """Return clean text from the raw rxiv xml content.

    Parameters
    ----------
    rxiv_xml : str
        The content of the rxiv full xml as obtained from the web.

    Returns
    -------
    str
        The text content stripped out from the raw full xml.
    """
    # FIXME: this is a very naive initial solution, we should instead
    # traverse the XML structure properly to get the content.
    text = re.sub('<.*?>', '', rxiv_xml)

```
