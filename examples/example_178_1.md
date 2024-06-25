# Description
Processing a single BEL statement and returning either the PybelProcessor or a single statement.

# Code
```
import pybel
import pybel.constants as pc
from pybel.io.sbel import add_sbel_row
from functools import lru_cache
import logging
logger = logging.getLogger(__name__)

class PybelProcessor:
    def __init__(self, graph):
        self.graph = graph
        self.statements = []
        self.annot_manager = type('', (object,), {'failures': {}})()  # Mock attributes for simplicity
    
    def get_statements(self):

def process_bel_stmt(bel: str, squeeze: bool = False):
    """Process a single BEL statement and return the PybelProcessor
    or a single statement if ``squeeze`` is True.

    Parameters
    ----------
    bel : str
        A BEL statement. See example below.
    squeeze : Optional[bool]
        If squeeze and there's only one statement in the processor,
        it will be unpacked.

    Returns
    -------
    statements : Union[Statement, PybelProcessor]
        A list of INDRA statments derived from the BEL statement.
        If squeeze is true and there was only one statement, the
        unpacked INDRA statement will be returned.

    Examples
    --------
    >>> from indra.sources.bel import process_bel_stmt
    >>> bel_s = 'kin(p(FPLX:MEK)) -> kin(p(FPLX:ERK))'
    >>> process_bel_stmt(bel_s, squeeze=True)
    Activation(MEK(kinase), ERK(), kinase)
    """
    r = pybel.parse(bel)
    # make sure activations in the right place
    for a, b in [(pc.SOURCE, pc.SOURCE_MODIFIER), (pc.TARGET, pc.TARGET_MODIFIER)]:
        side = r[a]
        for c in [pc.MODIFIER, pc.EFFECT, pc.FROM_LOC, pc.TO_LOC, pc.LOCATION]:
            if c in side:
                r.setdefault(b, {})[c] = side.pop(c)
    graph = pybel.BELGraph()
    add_sbel_row(graph, r)
    bp = process_pybel_graph(graph)
    if squeeze and len(bp.statements) == 1:
        return bp.statements[0]

```
