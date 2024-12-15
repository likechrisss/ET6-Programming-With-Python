def mystery_1(a, b):
    """
    Returns the sum of two inputs.

    Parameters:
        a: First input, can be an int, float, or string.
        b: Second input, can be an int, float, or string.

    Returns:
        The sum of the two inputs.

    Raises:
        TypeError: If inputs are incompatible for addition.

    """
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
