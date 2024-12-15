def mystery_3(a: int, b: int) -> int:
    """Compares two integers and returns based on the following logic:
    
    - If `a < b`, return `a`.
    - If `a > b`, return `b`.
    - If `a == b`, return their sum.

    Parameters:
        a: int, the first integer.
        b: int, the second integer.

    Returns -> int:
        An integer based on the comparison logic.

    Examples:
        >>> mystery_3(3, 5)
        3
        >>> mystery_3(7, 2)
        2
        >>> mystery_3(4, 4)
        8
    """
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
