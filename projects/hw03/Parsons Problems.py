'''
Q1: Neighbor Digits
Implement the function neighbor_digits. neighbor_digits takes in a positive 
integer num and an optional argument prev_digit. neighbor_digits outputs the 
number of digits in num that have the same digit to its right or left.
'''
def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    count = 0
    if num//10 == 0:
        return 0
    else:
        neighbor_digits(num//10)
        count += 1