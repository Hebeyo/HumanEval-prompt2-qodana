from typing import List, Any
def filter_integers(values: List[Any]) -> List[int]:
    res = []
    for x in values:
        if isinstance(x, int):
            res.append(x)
    return res
