def count_distinct_characters(string: str) -> int:
    return len(set([ch.lower() for ch in string]))
