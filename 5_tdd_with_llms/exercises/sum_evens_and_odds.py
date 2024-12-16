def sum_evens_and_odds(numbers):
    """
    Takes a list of numbers and returns a dictionary with 
    the sums of even and odd numbers.
    """
    return {
        "even": sum(num for num in numbers if num % 2 == 0),
        "odd": sum(num for num in numbers if num % 2 != 0)
    }
