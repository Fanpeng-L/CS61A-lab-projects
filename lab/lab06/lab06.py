def count_occurrences(t, n, x):
    """Return the number of times that x appears in the first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s2, 3, 10)
    2
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(s, 1, 3)
    1
    >>> count_occurrences(s, 4, 2)
    3
    >>> next(s)
    2
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> count_occurrences(s2, 6, 6)
    2
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for _ in range(n):
        value = next(t)
        if value == x:
            count += 1
    return count


def scale(it, multiplier):
    """Yield elements of the iterable it multiplied by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale([1, 2, 3, 4, 5, 6, 7, 8], 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    for item in it:
        yield item * multiplier


def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.

    >>> for num in hailstone(10):
    ...     print(num)
    10
    5
    16
    8
    4
    2
    1
    Pick a positive integer n as the start. If n is even, divide it by 2. 
    If n is odd, multiply it by 3 and add 1. Continue this process until n is 1.
    As an extra challenge, try writing a solution using recursion. 
    Since hailstone returns a generator, you can yield from a call to hailstone!
    """
    "*** YOUR CODE HERE ***"
    while n > 1:
        yield n 
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    yield n

# recursive solution:
def hailstone_re(n):
    yield n 
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            yield from hailstone_re(n//2)
        else:
            yield from hailstone_re(n * 3 + 1)