# Description
This example demonstrates how to use the TRIPS web service to process a text input, extract the resulting XML content, and save it to a file. It includes command-line options for specifying the input text or file and the output file.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import re
import sys
import getopt
import xml.dom.minidom
import logging
import requests

logger = logging.getLogger(__name__)

base_url = 'http://trips.ihmc.us/parser/cgi/'

def send_query(text, service_endpoint='drum', query_args=None, service_host=None):
    use_base_url = service_host if service_host else base_url
    if service_endpoint in ['drum', 'drum-dev', 'cwms', 'cwmsreader']:
        url = use_base_url + service_endpoint
    else:
        logger.error('Invalid service endpoint: %s' % service_endpoint)
        return ''
    if query_args is None:
        query_args = {}
    query_args.update({'input': text})
    res = requests.get(url, query_args, timeout=3600)
    if not res.status_code == 200:
        logger.error('Problem with TRIPS query: status code %s' % res.status_code)
        return ''
    return res.text

def get_xml(html, content_tag='ekb', fail_if_empty=False):
    cont = re.findall(r'<%(tag)s(.*?)>(.*?)</%(tag)s>' % {'tag': content_tag}, html, re.MULTILINE | re.DOTALL)
    if cont:
        events_terms = ''.join([l.strip() for l in cont[0][1].splitlines()])
        if 'xmlns' in cont[0][0]:
            meta = ' '.join([l.strip() for l in cont[0][0].splitlines()])
        else:
            meta = ''
    else:
        events_terms = ''
        meta = ''

    if fail_if_empty:
        assert events_terms != '', "Got empty string for events content from html:
%s" % html

    header = ('<?xml version="1.0" encoding="utf-8" standalone="yes"?><%s%s>' % (content_tag, meta))
    footer = '</%s>' % content_tag
    return header + events_terms.replace('\n', '') + footer

def save_xml(xml_str, file_name, pretty=True):
    try:
        fh = open(file_name, 'wt')
    except IOError:
        logger.error('Could not open %s for writing.' % file_name)
        return
    if pretty:
        xmld = xml.dom.minidom.parseString(xml_str)
        xml_str_pretty = xmld.toprettyxml()
        fh.write(xml_str_pretty)
    else:
        fh.write(xml_str)

if __name__ == '__main__':
    filemode = False
    text = 'Active BRAF phosphorylates MEK1 at Ser222.'
    outfile_name = 'braf_test.xml'

    opts, extraparams = getopt.getopt(sys.argv[1:], 's:f:o:h',
                                      ['string=', 'file=', 'output=', 'help'])
    for o, p in opts:
        if o in ['-h', '--help']:
            print('String mode: python -m indra.sources.trips.client.py '
                  '--string "RAS binds GTP" --output text.xml')
            print('File mode: python -m indra.sources.trips.client.py '
                  '--file test.txt --output text.xml')
            sys.exit()
        elif o in ['-s', '--string']:
            text = p
        elif o in ['-f', '--file']:
            filemode = True
            infile_name = p
        elif o in ['-o', '--output']:
            outfile_name = p

    if filemode:
        try:
            fh = open(infile_name, 'rt')
        except IOError:
            print('Could not open %s.' % infile_name)
            exit()
        text = fh.read()
        fh.close()
        print('Parsing contents of %s...' % infile_name)
    else:
        print('Parsing string: %s' % text)

    html = send_query(text)
    xml = get_xml(html)

```
