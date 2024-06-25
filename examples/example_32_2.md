# Description
Download text from ScienceDirect based on a search query, save the text files into a specified folder.

# Code
```
import os
import re
import logging
import textwrap
import datetime
import xml.etree.ElementTree as ET
import requests
from time import sleep
from indra.util import flatten
from indra import has_config, get_config
from functools import lru_cache, wraps
from indra.util import UnicodeXMLTreeBuilder as UTB

logger = logging.getLogger(__name__)

elsevier_api_url = 'https://api.elsevier.com/content'
elsevier_article_url_fmt = '%s/article/%%s' % elsevier_api_url
elsevier_search_url = '%s/search/sciencedirect' % elsevier_api_url

ELSEVIER_KEYS = None
API_KEY_ENV_NAME = 'ELSEVIER_API_KEY'
INST_KEY_ENV_NAME = 'ELSEVIER_INST_KEY'


def _ensure_api_keys(task_desc, failure_ret=None):
    def check_func_wrapper(func):
        @wraps(func)
        def check_api_keys(*args, **kwargs):
            global ELSEVIER_KEYS
            if ELSEVIER_KEYS is None:
                ELSEVIER_KEYS = {}
                if not has_config(INST_KEY_ENV_NAME):
                    logger.warning('Institution API key %s not found in config '
                                   'file or environment variable: this will '
                                   'limit access for %s'
                                   % (INST_KEY_ENV_NAME, task_desc))
                ELSEVIER_KEYS['X-ELS-Insttoken'] = get_config(INST_KEY_ENV_NAME)
                if not has_config(API_KEY_ENV_NAME):
                    logger.error('API key %s not found in configuration file '
                                 'or environment variable: cannot %s'
                                 % (API_KEY_ENV_NAME, task_desc))
                    return failure_ret
                ELSEVIER_KEYS['X-ELS-APIKey'] = get_config(API_KEY_ENV_NAME)
            elif 'X-ELS-APIKey' not in ELSEVIER_KEYS.keys():
                logger.error('No Elsevier API key %s found: cannot %s'
                             % (API_KEY_ENV_NAME, task_desc))
                return failure_ret
            return func(*args, **kwargs)
        return check_api_keys
    return check_func_wrapper


@_ensure_api_keys('perform search')
def search_science_direct(query_str, field_name, year=None, loaded_after=None):
    count = 100
    params = {'qs': query_str,
              'display': {
                  'offset': 0,
                  'show': count,
                  'sortBy': 'date'},
              'field': 'pii'}
    if year:
        params['date'] = year
    if loaded_after:
        params['loadedAfter'] = loaded_after
    all_parts = []
    while True:
        res = requests.put(
            elsevier_search_url, json=params, headers=ELSEVIER_KEYS)
        if not res.status_code == 200:
            logger.info('Got status code: %d' % res.status_code)
            break
        res_json = res.json()
        total_results = res_json['resultsFound']
        if total_results == 0:
            logger.info('Search result was empty')
            return []
        try:
            entries = res_json['results']
        except KeyError:
            entries = []
        parts = [entry[field_name] for entry in entries]
        all_parts += parts
        cont = False
        if (params['display']['offset'] + count) <= min(total_results, 6000):
            params['display']['offset'] += count
            cont = True
            sleep(1)
        if not cont:
            break
    return all_parts

@_ensure_api_keys('download article')
def download_article(id_val, id_type='doi', on_retry=False):
    if id_type == 'pmid':
        id_type = 'pubmed_id'
    url = '%s/%s' % (elsevier_article_url_fmt % id_type, id_val)
    params = {'httpAccept': 'text/xml'}
    res = requests.get(url, params, headers=ELSEVIER_KEYS)
    if res.status_code == 404:
        logger.info("Resource for %s not available on elsevier." % url)
        return None
    elif res.status_code == 429:
        if not on_retry:
            logger.warning("Broke the speed limit. Waiting half a second then "
                           "trying again...")
            sleep(0.5)
            return download_article(id_val, id_type, True)
        else:
            logger.error("Still breaking speed limit after waiting.")
            logger.error("Elsevier response: %s" % res.text)
            return None
    elif res.status_code != 200:
        logger.error('Could not download article %s: status code %d' %
                     (url, res.status_code))
        logger.error('Elsevier response: %s' % res.text)
        return None
    else:
        content_str = res.content.decode('utf-8')
        if content_str.startswith('<service-error>'):
            logger.error('Got a service error with 200 status: %s'
                         % content_str)
            return None
    return content_str


def extract_text(xml_string):
    paragraphs = extract_paragraphs(xml_string)
    if paragraphs:
        return '\n'.join(re.sub(r'\s+', ' ', p) for p in paragraphs) + '\n'
    else:
        return None


def extract_paragraphs(xml_string):
    xml_tree = ET.XML(xml_string.encode('utf-8'), parser=UTB())
    full_text = xml_tree.find('article:originalText', elsevier_ns)
    if full_text is None:
        logger.info('Could not find full text element article:originalText')
        return None
    article_body = _get_article_body(full_text)
    if article_body:
        return article_body
    raw_text = _get_raw_text(full_text)
    if raw_text:
        return [raw_text]
    return None


def _get_article_body(full_text_elem):
    possible_paths = [
        'xocs:doc/xocs:serial-item/ja:article/ja:body',
        'xocs:doc/xocs:serial-item/ja:simple-article/ja:body',
        'xocs:doc/xocs:serial-item/ja:converted-article/ja:body',
        'xocs:doc/xocs:nonserial-item/book:chapter',
        'xocs:doc/xocs:nonserial-item/book:fb-non-chapter'
        ]
    for pth in possible_paths:
        main_body = full_text_elem.find(pth, elsevier_ns)
        if main_body is not None:
            logger.info("Found main body element: \"%s\"" % pth)
            return _get_sections(main_body)
        logger.info("Could not find main body element: \"%s\"." % pth)
    return None


def _get_sections(main_body_elem):
    possible_paths = ['common:sections/common:section', 'common:section',
                      'common:sections']
    for pth in possible_paths:
        sections = main_body_elem.findall(pth, elsevier_ns)
        if len(sections):
            logger.info("Found sections in main body using \"%s\"" % pth)
            break
        logger.info("Found no sections in main body with \"%s\"" % pth)
    else:
        return None

    paragraphs = []
    for s in sections:
        pars = s.findall('common:para', elsevier_ns)
        pars += s.findall('common:section/common:para', elsevier_ns)
        for p in pars:
            content = ' '.join(p.itertext())
            paragraphs.append(content)
    return paragraphs


def _get_raw_text(full_text_elem):
    raw_text = full_text_elem.find('xocs:doc/xocs:rawtext', elsevier_ns)
    if raw_text is None:
        logger.info("Could not find rawtext element xocs:doc/xocs:rawtext")
        return None
    else:
        logger.info("Found rawtext element xocs:doc/xocs:rawtext")

def download_from_search(query_str, folder, do_extract_text=True,
                         max_results=None):
    """Save raw text files based on a search for papers on ScienceDirect.

    This performs a search to get PIIs, downloads the XML corresponding to
    the PII, extracts the raw text and then saves the text into a file
    in the designated folder.

    Parameters
    ----------
    query_str : str
        The query string to search with
    folder : str
        The local path to an existing folder in which the text files
        will be dumped
    do_extract_text : bool
        Choose whether to extract text from the xml, or simply save the raw xml
        files. Default is True, so text is extracted.
    max_results : int or None
        Default is None. If specified, limit the number of results to the given
        maximum.
    """
    piis = get_piis(query_str)
    for pii in piis[:max_results]:
        if os.path.exists(os.path.join(folder, '%s.txt' % pii)):
            continue
        logger.info('Downloading %s' % pii)
        xml = download_article(pii, 'pii')
        sleep(1)
        if do_extract_text:
            txt = extract_text(xml)
            if not txt:
                continue

            with open(os.path.join(folder, '%s.txt' % pii), 'wb') as fh:
                fh.write(txt.encode('utf-8'))
        else:
            with open(os.path.join(folder, '%s.xml' % pii), 'wb') as fh:
                fh.write(xml.encode('utf-8'))

```
