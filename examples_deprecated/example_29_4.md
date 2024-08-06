# Description
Extracting the base URL to full text format from the landing page content for an rxiv paper.

# Code
```

def get_text_url_base(content):
    """Return base URL to full text based on the content of the landing page.

    Parameters
    ----------
    content : str
        The content of the landing page for an rxiv paper.

    Returns
    -------
    str or None
        The base URL if available, otherwise None.
    """
    match = re.match('(?:.*)"citation_html_url" content="([^"]+).full"',
                     content, re.S)
    if match:
        return match.groups()[0]

```
