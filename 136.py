def largest_smallest_integers(lst):
    smallest = None
    largest = None
    for i in lst:
        if i < 0 and (smallest is None or i > smallest):
            smallest = i
        if i > 0 and (largest is None or i < largest):
            largest = i
    return (smallest, largest)
