def divisible_by_11(number):
    """
    Uses above criterion to check if number is divisible by 11

    For example:

        >>> import main
        >>> main.divisible_by_11(11)
        True
        >>> main.divisible_by_11(12)
        False

    """
    string_number = str(number)
    alternating_sum = sum((-1) ** i * int(d) for i, d
                           in enumerate(string_number))
    return alternating_sum == 0
