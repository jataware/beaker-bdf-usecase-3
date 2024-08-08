# Description
Shows how to process a sentence using TRIPS processor.

# Code
```

def test_getting_started3():
    # Chunk 3
    from indra.sources import trips
    sentence = 'MAP2K1 phosphorylates MAPK3 at Thr-202 and Tyr-204'
    trips_processor = trips.process_text(sentence)

```
