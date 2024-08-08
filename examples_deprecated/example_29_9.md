# Description
Main script to obtain metadata and text content from bioRxiv, including fetching covid-19 related publications and saving their contents in a JSON file.

# Code
```
import os
import json
import requests
import datetime

collection_url = 'https://connect.biorxiv.org/relate/collection_json.php?grp='
covid19_collection_id = '181'

\
def get_collection_pubs(collection_id, min_date=None):
    res = requests.get(collection_url + collection_id)
    res.raise_for_status()
    pubs = res.json()['rels']
    if min_date:
        new_rels = []
        for pub in pubs:
            try:
                date = datetime.datetime.strptime(pub.get('rel_date'), '%Y-%m-%d')
            except Exception:
                continue
            if date >= min_date:
                new_rels.append(pub)
        return new_rels
    return pubs


def get_pdf_xml_url_base(content):
    match = re.match('(?:.*)"citation_pdf_url" content="([^"]+).full.pdf"', content, re.S)
    if match:
        return match.groups()[0]
    return None


def get_text_url_base(content):
    match = re.match('(?:.*)"citation_html_url" content="([^"]+).full"', content, re.S)
    if match:
        return match.groups()[0]
    return None


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


def get_content_from_pub_json(pub, format):
    if format == 'abstract':
        return pub.get('rel_abstract')
    formats = get_formats(pub)
    if format not in formats:
        logger.warning('Content not available in format %s' % format)
        return None
    if format == 'abstract':
        return formats.get('abstract')
    elif format == 'pdf':
        return requests.get(formats[format]).content
    elif format == 'xml':
        return get_text_from_rxiv_xml(requests.get(formats[format]).text)
    elif format == 'txt':
        return get_text_from_rxiv_text(requests.get(formats[format]).text)


def get_text_from_rxiv_xml(rxiv_xml):
    text = re.sub('<.*?>', '', rxiv_xml)
    return text


def get_text_from_rxiv_text(rxiv_text):
    lines = [line.strip() for line in rxiv_text.split('\n') if line.strip()]
    current_section = 'title'
    text = lines[0] + '\n'
    line_idx = 1
    skip_section = {'References', 'Footnotes', 'Acknowledgements', 'Supplementary Figures', 'Declaration of Interests', 'Author Contributions', 'Code and data availability'}
    for line in lines[line_idx:]:
        line_idx += 1
        match = re.match('## (.+)', line)
        if match:
            current_section = match.groups()[0]
            break
    while line_idx < len(lines):
        for line in lines[line_idx:]:
            line_idx += 1
            match_heading = re.match('## (.+)', line)
            match_subheading = re.match('### (.+)', line)
            if match_heading:
                current_section = match_heading.groups()[0]
                break
            elif current_section in skip_section:
                continue
            elif match_subheading:
                text += (match_subheading.groups()[0] + '\n')
            else:
                text += (line + '\n')

if __name__ == '__main__':
    import os
    import json
    fname = 'covid19_pubs.json'
    if os.path.exists(fname):
        with open(fname, 'r') as fh:
            covid19_pubs = json.load(fh)
    else:
        covid19_pubs = get_collection_pubs(covid19_collection_id)
        with open(fname, 'w') as fh:
            json.dump(covid19_pubs, fh)
    contents = {}
    for pub in covid19_pubs:
        doi = pub['rel_doi']
        formats = get_formats(pub)
        if 'txt' in formats:
            print('Getting text for %s' % doi)
            txt = get_content_from_pub_json(pub, 'txt')
        elif 'xml' in formats:
            print('Getting xml for %s' % doi)
            txt = get_content_from_pub_json(pub, 'xml')
        else:
            print('Getting abstract for %s' % doi)
            txt = get_content_from_pub_json(pub, 'abstract')
        contents[doi] = txt
    with open('covid19_contents', 'w') as fh:

```
