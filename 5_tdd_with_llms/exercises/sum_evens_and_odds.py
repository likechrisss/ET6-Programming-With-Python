def sum_evens_and_odds(numbers):
    """
    Takes a list of numbers and returns a dictionary with 
    the sums of even and odd numbers.
    """
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return {"even": even_sum, "odd": odd_sum}
