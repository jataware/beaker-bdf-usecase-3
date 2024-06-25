# Description
Example of how to read a given PMC article using the DrumReader class.

# Code
```
from kqml import KQMLModule, KQMLPerformative, KQMLList
import random
import logging
logger = logging.getLogger(__name__)

class DrumReader(KQMLModule):
    def __init__(self, **kwargs):
        # Initialization logic
        self.msg_counter = random.randint(1, 100000)
        self.extractions = []
        self.reply_counter = 0

    def send(self, msg):
        # Placeholder for send method

    def read_pmc(self, pmcid):
        """Read a given PMC article.

        Parameters
        ----------
        pmcid : str
            The PMC ID of the article to read. Note that only
            articles in the open-access subset of PMC will work.
        """
        msg = KQMLPerformative('REQUEST')
        msg.set('receiver', 'READER')
        content = KQMLList('run-pmcid')
        content.sets('pmcid', pmcid)
        content.set('reply-when-done', 'true')
        msg.set('content', content)
        msg.set('reply-with', 'P-%s' % pmcid)
        self.reply_counter += 1

```
