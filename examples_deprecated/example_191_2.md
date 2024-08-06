# Description
Process text to return mentions JSON object using the Eidos reader.

# Code
```
import os
import json
import datetime
from indra import get_config
from indra.java_vm import autoclass

eidos_package = 'org.clulab.wm.eidos'

class EidosReader(object):
    def __init__(self):
        self.eidos_reader = None
        self.default_ontology = None

    def initialize_reader(self):
        eidos = autoclass(eidos_package + '.EidosSystem')
        self.eidos_reader = eidos()

def _list_to_seq(lst):
    ml = autoclass('scala.collection.mutable.MutableList')()
    for element in lst:
        ml.appendElem(element)

    def process_text(self, text):
        """Return a mentions JSON object given text.

        Parameters
        ----------
        text : str
            Text to be processed.

        Returns
        -------
        json_dict : dict
            A JSON object of mentions extracted from text.
        """
        if self.eidos_reader is None:
            self.initialize_reader()
        default_arg = lambda x: autoclass('scala.Some')(x)
        today = datetime.date.today().strftime("%Y-%m-%d")
        fname = 'default_file_name'

        annot_doc = self.eidos_reader.extractFromText(
            text,
            False,  # CAG-relevant only
            default_arg(today),  # doc creation time
            default_arg(fname)  # file name
            )
        # We need to get a Scala Seq of annot docs here
        ml = _list_to_seq([annot_doc])
        # We currently do not need toinstantiate the adjective grounder
        # if we want to reinstate it, we would need to do the following
        # ag = EidosAdjectiveGrounder.fromConfig(
        #   EidosSystem.defaultConfig.getConfig("adjectiveGrounder"))
        # We now create a JSON-LD corpus
        jc = autoclass(eidos_package + '.serialization.jsonld.JLDCorpus')
        corpus = jc(ml)
        # Finally, serialize the corpus into JSON string
        mentions_json = corpus.toJsonStr()
        json_dict = json.loads(mentions_json)

```
