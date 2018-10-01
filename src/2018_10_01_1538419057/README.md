# 2018_10_01_1538419057 - Sum Exists
Given the following method signature:

```python
from typing import List

def sum_exits(a: List[int], b: List[int]) -> bool:
    pass
```

Provide a solution that checks if there are 2 values in `a` that produce a sum equal to a value that exists in `b`.

Examples: 
- `a: [1, 2], b: [3]`   ->  True
- `a: [1, 2], b: [4]`   ->  False
- `a: [2, 2], b: [4]`   ->  True
- `a: [0, 2], b: [4]`   ->  False
- `a: [-1, 4], b: [3]`  ->  True
- `a: [-1, 4], b: [4]`  ->  False
