# Description
Extracting the base URL to PDF or XML format from the landing page content for an rxiv paper.

# Code
```

def get_pdf_xml_url_base(content):
    """Return base URL to PDF/XML based on the content of the landing page.

    Parameters
    ----------
    content : str
        The content of the landing page for an rxiv paper.

    Returns
    -------
    str or None
        The base URL if available, otherwise None.
    """
    match = re.match('(?:.*)"citation_pdf_url" content="([^"]+).full.pdf"',
                     content, re.S)
    if match:
        return match.groups()[0]

```
