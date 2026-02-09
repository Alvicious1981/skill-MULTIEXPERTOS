def find_items(list_a, list_b):
    # O(n^2) loop instead of using a set
    return [item for item in list_a if item in list_b]