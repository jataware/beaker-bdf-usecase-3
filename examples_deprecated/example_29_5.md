# Description
Getting available formats for a publication from JSON data, including parsing URLs for PDF, XML, and text formats.

# Code
```
import requests
import re

def get_pdf_xml_url_base(content):
    match = re.match('(?:.*)"citation_pdf_url" content="([^"]+).full.pdf"', content, re.S)
    if match:
        return match.groups()[0]
    return None


def get_text_url_base(content):
    match = re.match('(?:.*)"citation_html_url" content="([^"]+).full"', content, re.S)
    if match:
        return match.groups()[0]

def get_formats(pub):
    """Return formats available for a publication JSON.

    Parameters
    ----------
    pub : dict
        The JSON dict description a publication.

    Returns
    -------
    dict
        A dict with available formats as its keys (abstract, pdf, xml, txt)
        and either the content (in case of abstract) or the URL
        (in case of pdf, xml, txt) as the value.
    """
    formats = {}
    if 'rel_abs' in pub:
        formats['abstract'] = pub['rel_abs']
    # The publication JSON does not contain enough information generally
    # to identify the URL for the various formats. Therefore we have to
    # load the landing page for the article and parse out various URLs
    # to reliably get to the desired content.
    landing_page_res = requests.get(pub['rel_link'])

    # The URL for the full PDF and XML is often different in format than
    # the rel_site URL so we need to get the link to it from the content
    # of the landing page. The XML URL doesn't explicitly appear in the
    # page content therefore we work with the citation_pdf_url and get
    # URLs for both the PDF and the XML.
    pdf_xml_url_base = get_pdf_xml_url_base(landing_page_res.text)
    if pdf_xml_url_base:
        formats['pdf'] = pdf_xml_url_base + '.full.pdf'
        formats['xml'] = pdf_xml_url_base + '.source.xml'
    text_url_base = get_text_url_base(landing_page_res.text)
    if text_url_base:
        formats['txt'] = text_url_base + 'txt'

```
