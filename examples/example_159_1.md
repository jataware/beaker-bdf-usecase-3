# Description
Generate a source color data structure with source names and their corresponding styles.

# Code
```
import logging
from indra.sources import SOURCE_INFO

def _source_info_to_source_colors(
        source_info: Optional[SourceInfo] = None
) -> SourceColors:
    """Returns a source color data structure with source names as they
    appear in INDRA DB
    """
    if source_info is None:
        source_info = SOURCE_INFO
        every_source = all_sources
    else:
        every_source = []
        for source in source_info:
            every_source.append(source)

    # Initialize dicts for source: background-color for readers and databases
    database_colors = {}
    reader_colors = {}
    for source in every_source:
        # Get name as it is registered in source_info.json and get info
        src_info_name = reverse_source_mappings.get(source, source)
        info = source_info.get(src_info_name)
        if not info:
            logger.error('Source info missing for %s' % source)
            continue
        # Get color from info
        color = info['default_style']['background-color']

        # Map back to db name, use original name from all_sources as default
        mapped_source = internal_source_mappings.get(src_info_name, source)
        if info['type'] == 'reader':
            reader_colors[mapped_source] = color
        else:
            database_colors[mapped_source] = color

    return [('databases', {'color': DB_TEXT_COLOR,
                           'sources': database_colors}),
            ('reading', {'color': READER_TEXT_COLOR,

```
