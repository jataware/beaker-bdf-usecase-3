# Description
Example of how to read a given text phrase using the DrumReader class.

# Code
```
from kqml import KQMLModule, KQMLPerformative, KQMLList
import random
import logging
logger = logging.getLogger(__name__)

def _get_perf(text, msg_id):
    msg = KQMLPerformative('REQUEST')
    msg.set('receiver', 'READER')
    content = KQMLList('run-text')
    content.sets('text', text)
    msg.set('content', content)
    msg.set('reply-with', msg_id)
    return msg

class DrumReader(KQMLModule):
    def __init__(self, **kwargs):
        # Initialization logic
        self.msg_counter = random.randint(1, 100000)
        self.extractions = []
        self.reply_counter = 0

    def send(self, msg):
        # Placeholder for send method

    def read_text(self, text):
        """Read a given text phrase.

        Parameters
        ----------
        text : str
            The text to read. Typically a sentence or a paragraph.
        """
        logger.info('Reading: "%s"' % text)
        msg_id = 'RT000%s' % self.msg_counter
        kqml_perf = _get_perf(text, msg_id)
        self.reply_counter += 1
        self.msg_counter += 1

```
