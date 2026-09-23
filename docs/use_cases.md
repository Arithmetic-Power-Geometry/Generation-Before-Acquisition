# Where RFS could be used

## Good-fit workloads

1. Distributed records: metadata comparisons are cheap; fetching or moving full records is expensive.
2. Persistent memory / flash: writes differ substantially from reads/comparisons.
3. Database engines: order may be partly known from indexes, zone maps, partitions or min/max metadata.
4. Scientific data: approximate/cached descriptors are cheap, exact key evaluation is expensive.
5. Sensor or measurement ranking: cheap proxies coexist with costly exact measurements.
6. Heterogeneous compute: CPU, GPU, storage and network actions have different energy/time/movement costs.

## Poor-fit workloads

- small primitive arrays already resident in RAM;
- random arbitrary keys with no side information;
- workloads where all operations have nearly identical cost;
- cases where optimized library sort dominates constants.

RFS should be evaluated by total resource cost, not by wall-clock time alone.
