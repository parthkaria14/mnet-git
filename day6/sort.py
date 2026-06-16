def sort_descending(numbers):
    """Return a new list of numbers sorted from largest to smallest.

    Args:
        numbers: A list of numbers to sort.

    Returns:
        A new list in descending order. Returns an empty list if the
        input is empty.
    """
    if not numbers:
        return []
    return sorted(numbers, reverse=True)
