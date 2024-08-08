# Description
This example demonstrates how to initialize the SBGNAssembler class with INDRA Statements and assemble an SBGN model into an XML string.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import copy
import logging
import lxml.etree
import lxml.builder
from indra.statements import *
from indra.assemblers.pysb.assembler import PysbPreassembler

logger = logging.getLogger(__name__)

sbgn_ns = 'http://sbgn.org/libsbgn/0.2'

class SBGNAssembler(object):
    """This class assembles an SBGN model from a set of INDRA Statements.

    The Systems Biology Graphical Notation (SBGN) is a widely used
    graphical notation standard for systems biology models.
    This assembler creates SBGN models following the Process Desctiption (PD)
    standard, documented at:
    https://github.com/sbgn/process-descriptions/blob/master/UserManual/sbgn_PD-level1-user-public.pdf.
    For more information on SBGN, see: http://sbgn.github.io/sbgn/

    Parameters
    ----------
    stmts : Optional[list[indra.statements.Statement]]
        A list of INDRA Statements to be assembled.

    Attributes
    ----------
    statements : list[indra.statements.Statement]
        A list of INDRA Statements to be assembled.
    sbgn : lxml.etree.ElementTree
        The structure of the SBGN model that is assembled, represented as an
        XML ElementTree.
    """

    process_style = {'x': '0', 'y': '0', 'w': '10', 'h': '10'}
    source_sink_style = {'x': '0', 'y': '0', 'w': '10', 'h': '10'}
    monomer_style = {'x': '0', 'y': '0', 'w': '60', 'h': '30'}
    complex_style = {'x': '1', 'y': '1', 'w': '60', 'h': '65'}
    entity_type_style = {'x': '0', 'y': '0', 'w': '30', 'h': '12'}
    entity_state_style = {'x': '1', 'y': '1', 'w': '28', 'h': '12'}

    def __init__(self, statements=None):
        if not statements:
            self.statements = []
        else:
            self.statements = statements
        self.sbgn = emaker.sbgn()
        self._map = emaker.map(language='process description')
        self.sbgn.append(self._map)
        self._id_counter = 0
        self._agent_ids = {}

    def add_statements(self, stmts):
        """Add INDRA Statements to the assembler's list of statements.

        Parameters
        ----------
        stmts : list[indra.statements.Statement]
            A list of :py:class:`indra.statements.Statement`
            to be added to the statement list of the assembler.
        """
        for stmt in stmts:
            if not self.statement_exists(stmt):
                self.statements.append(stmt)

    def make_model(self):
        """Assemble the SBGN model from the collected INDRA Statements.

        This method assembles an SBGN model from the set of INDRA Statements.
        The assembled model is set as the assembler's sbgn attribute (it is
        represented as an XML ElementTree internally). The model is returned
        as a serialized XML string.

        Returns
        -------
        sbgn_str : str
            The XML serialized SBGN model.
        """
        ppa = PysbPreassembler(self.statements)
        ppa.replace_activities()
        self.statements = ppa.statements
        self.sbgn = emaker.sbgn()
        self._map = emaker.map()
        self.sbgn.append(self._map)
        for stmt in self.statements:
            if isinstance(stmt, Modification):
                self._assemble_modification(stmt)
            elif isinstance(stmt, RegulateActivity):
                self._assemble_regulateactivity(stmt)
            elif isinstance(stmt, RegulateAmount):
                self._assemble_regulateamount(stmt)
            elif isinstance(stmt, Complex):
                self._assemble_complex(stmt)
            elif isinstance(stmt, ActiveForm):
                #self._assemble_activeform(stmt)
                pass
            else:
                logger.warning("Unhandled Statement type %s" % type(stmt))
                continue
        sbgn_str = self.print_model()

```
