# Description
The `get_gap_gef` method to extract Gap and Gef INDRA Statements.

# Code
```
indra.statements import *
indra.util import flatten

    def get_gap_gef(self):
        """Extract Gap and Gef INDRA Statements."""
        for gap_gef, ev, control, conversion in \
                self._control_conversion_iter(bp.Conversion, 'primary'):
            assert isinstance(gap_gef, Agent)
            # We have to make sure that we don't pick up chemicals here
            if not set(gap_gef.db_refs.keys()) & {'HGNC', 'UP'}:
                continue
            left_complexes = [bpe for bpe in conversion.left
                              if _is_complex(bpe)]
            right_complexes = [bpe for bpe in conversion.right
                               if _is_complex(bpe)]
            left_ras, left_gtp_gdp = \
                self.find_gdp_gtp_complex(left_complexes)
            right_ras, right_gtp_gdp = \
                self.find_gdp_gtp_complex(right_complexes)
            if left_gtp_gdp == 'GDP' and right_gtp_gdp == 'GTP':
                stmt_type = Gef
            elif left_gtp_gdp == 'GTP' and right_gtp_gdp == 'GDP':
                stmt_type = Gap
            else:
                continue

            ras_agents = self._get_agents_from_entity(left_ras)
            for ras in _listify(ras_agents):
                st = stmt_type(gap_gef, ras, evidence=ev)

```
