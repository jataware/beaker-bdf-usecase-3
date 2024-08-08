# Description
Invoking TEES and converting the output into a networkx graph, including parsing sentence segmentation XML, TEES .a1 entity files, and TEES .a2 event files.

# Code
```
import networkx as nx
from lxml import etree

class TEESSentences:
    ...

class TEESEntity:
    ...

def parse_a1(a1_text):
    ...

def parse_a2(a2_text, entities, tees_sentences):

def parse_output(a1_text, a2_text, sentence_segmentations):
    """Parses the output of the TEES reader and returns a networkx graph
    with the event information.

    Parameters
    ----------
    a1_text : str
        Contents of the TEES a1 output, specifying the entities
    a1_text : str
        Contents of the TEES a2 output, specifying the event graph
    sentence_segmentations : str
        Concents of the TEES sentence segmentation output XML

    Returns
    -------
    events : networkx.DiGraph
        networkx graph with the entities, events, and relationship between
        extracted by TEES
    """

    # Parse the sentence segmentation document
    tees_sentences = TEESSentences(sentence_segmentations)

    # Parse the a1 (entities) file
    entities = parse_a1(a1_text)

    # Parse the a2 (events) file
    events = parse_a2(a2_text, entities, tees_sentences)


```
