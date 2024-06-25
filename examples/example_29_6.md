# Description
Obtaining text content based on the specified format (abstract, pdf, txt, xml) from a publication JSON.

# Code
```
import requests
import re
import logging

logger = logging.getLogger(__name__)

\
def get_formats(pub):
    formats = {}
    if 'rel_abs' in pub:
        formats['abstract'] = pub['rel_abs']
    landing_page_res = requests.get(pub['rel_link'])
    pdf_xml_url_base = get_pdf_xml_url_base(landing_page_res.text)
    if pdf_xml_url_base:
        formats['pdf'] = pdf_xml_url_base + '.full.pdf'
        formats['xml'] = pdf_xml_url_base + '.source.xml'
    text_url_base = get_text_url_base(landing_page_res.text)
    if text_url_base:
        formats['txt'] = text_url_base + 'txt'
    return formats


def get_pdf_xml_url_base(content):
    match = re.match('(?:.*)"citation_pdf_url" content="([^"]+).full.pdf"', content, re.S)
    if match:
        return match.groups()[0]
    return None


def get_text_url_base(content):
    match = re.match('(?:.*)"citation_html_url" content="([^"]+).full"', content, re.S)
    if match:
        return match.groups()[0]

def get_content_from_pub_json(pub, format):
    """Get text content based on a given format from a publication JSON.

    In the case of abstract, the content is returned
    from the JSON directly. For pdf, the content is returned as bytes
    that can be dumped into a file. For txt and xml, the text is processed
    out of either the raw XML or text content that rxiv provides.

    Parameters
    ----------
    pub : dict
        The JSON dict description a publication.
    format : str
        The format, if available, via which the content should be
        obtained.
    """
    if format == 'abstract':
        return pub.get('rel_abstract')

    formats = get_formats(pub)
    if format not in formats:
        logger.warning('Content not available in format %s' % format)
        return None

    # If we're looking for an abstract, that is directly accessible
    # in the pub JSON so we can just return it
    if format == 'abstract':
        return formats.get('abstract')
    # For PDFs we return the result in bytes that can then be dumped
    # into a file.
    elif format == 'pdf':
        return requests.get(formats[format]).content
    # For xml and text, we return the result as str
    elif format == 'xml':
        return get_text_from_rxiv_xml(requests.get(formats[format]).text)
    elif format == 'txt':

```
