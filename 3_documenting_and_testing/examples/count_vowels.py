#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting vowels in a string.

Module contents:
    - count_vowels: counts the number of vowels in a string.

Created on XX XX XX
@author: Evan Cole + Claude AI
"""
# Added some new Edge cases that could be helpful
def count_vowels(text: str) -> int:
    """Count the number of vowels (a, e, i, o, u) in a string.

    Parameters:
        text: str, the input string to check

    Returns -> int: number of vowels in the text

    Raises:
        TypeError: if the argument is not a string

    >>> count_vowels("hello")
    2
    >>> count_vowels("APPLE")
    2
    >>> count_vowels("why")
    0
    >>> count_vowels("")
    0
    >>> count_vowels("12345")
    0
    >>> count_vowels("AEIOUaeiou")
    10
    >>> count_vowels("!@#$%^&*()")
    0
    """
    if not isinstance(text, str):
        raise TypeError("input must be a string")

    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)
