def mystery_2(a: list) -> int | None:
    """Returns the length of a list or None if the list is empty.

    Examples:
        >>> mystery_2([])
        None
        >>> mystery_2([1, 2, 3])
        3
    """
    return None if len(a) == 0 else len(a)
