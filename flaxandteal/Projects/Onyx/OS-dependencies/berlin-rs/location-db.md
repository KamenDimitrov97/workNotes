### Description
Manages a database of locations. LocationsDb struct defined here.

### Imports

1. Standard library:
```rust
std::boxed::Box, //  Smart pointers for heap allocation. Allows storage of large data on the heap instead of the stack, useful for managing memory for complex data structures.
std::error::Error, // error handling.
std::fs::File, // Read/Write data to/from files
std::io::BufReader, // I/O reader
std::path::PathBuf, // Manages filesystem paths, providing a mutable and owned version of 'Path'
std::sync::RwLock // Read/Write lock
std::time::Instant // Measures time
```
2. External crates:
```rust
use csv::ReaderBuilder; // csv builder
use fst::{Automaton, Streamer}; // Used to create and search through a finite state transducer (FST) for efficiently managing and querying sets of strings.
use indextree::{Arena, NodeId}; // tree data structure
use rayon::iter::{
    IndexedParallelIterator, IntoParallelIterator, IntoParallelRefIterator, ParallelBridge,
    ParallelIterator,
}; // Facilitates parallel processing of iterators to speed up tasks like data parsing and searching, leveraging multiple CPU cores.
use serde_json::Value; // parsing json
use tracing::{debug, info}; // logs
use ustr::{Ustr, UstrMap, UstrSet}; // unique strings
```

3. Custom Imports:

```rust
use crate::graph::ResultsGraph;
use crate::location::{AnyLocation, CsvLocode, LocData, Location};
use crate::search::{Score, SearchTerm};
use crate::SEARCH_INCLUSION_THRESHOLD;
```

### Public method retrieve 

Retrieves a location from the database using a matchable string.
This method attempts to find an unique string for the matchable input. If found and the length of the string is greater than one, it retrieves the corresponding Location from the all map.

