from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    res = []
    for n in numbers:
        if numbers.count(n) <= 1:
            res.append(n)
    return res
