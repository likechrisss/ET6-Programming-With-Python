def repeat_character(s: str, char: str, n: int) -> str:
    # Minimal implementation just to pass the test, this is step 2
    result = []
    for c in s:
        if c == char:
            result.append(c * n)
        else:
            result.append(c)
    return "".join(result)
