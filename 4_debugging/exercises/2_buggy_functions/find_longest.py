#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the longest string in a list.

Module contents:
    - find_longest: Finds the longest string in a list of strings.

Created on 2024-12-06
Author: Claude AI
"""

def find_longest(items: list) -> str:
    """Finds the longest string in a list of strings.

    If multiple strings tie for longest length, the first one
    encountered is returned. Empty strings are valid candidates.

    Parameters:
        items: list of strings to search

    Returns -> str: the longest string in the list

    Raises:
        AssertionError: if input is not a list or contains non-strings
        ValueError: if the list is empty

    Examples:
        # Standard cases
        >>> find_longest(['a', 'bb', 'ccc'])
        'ccc'
        >>> find_longest(['ccc', 'bb', 'a'])
        'ccc'
        >>> find_longest(['hi', 'hello', 'hey', 'howdy'])
        'hello'

        # Edge cases
        >>> find_longest(['', 'a', 'bb'])
        'bb'
        >>> find_longest(['a', '', 'bb'])
        'bb'
        >>> find_longest(['', '', ''])
        ''
        >>> find_longest(['abc', 'def', 'ghi'])
        'abc'

        # Defensive tests
        >>> find_longest([])
        Traceback (most recent call last):
            ...
        ValueError: list cannot be empty
        >>> find_longest("hello")
        Traceback (most recent call last):
            ...
        AssertionError: input must be a list
        >>> find_longest(['hello', 42, 'world'])
        Traceback (most recent call last):
            ...
        AssertionError: all items must be strings
    """
    # Ensure input is a list
    assert isinstance(items, list), "input must be a list"
    # Ensure all items in the list are strings
    assert all(isinstance(item, str) for item in items), "all items must be strings"
    # Handle empty list
    if not items:
        raise ValueError("list cannot be empty")
    
    # Initialize the longest string as the first element
    longest = items[0]
    for item in items:
        if len(item) > len(longest):
            longest = item
    return longest
