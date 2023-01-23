'''
Q1: Warm Up: Recursive Multiplication
These exercises are meant to help refresh your memory of the topics covered in 
lecture.
Write a function that takes two numbers m and n and returns their product. 
Assume m and n are positive integers. Use recursion, not mul or *.
Hint: 5 * 3 = 5 + (5 * 2) = 5 + 5 + (5 * 1).
'''

def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n-1)
multiply(2,3)


'''Q3: Find the Bug'''
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2 and n >=0:
        return n
    else:
        return n * skip_mul(n - 2)
print(skip_mul(8))


'''
Q4: Recursive Hailstone
Recall the hailstone function from Homework 2. 
First, pick a positive integer n as the start. If n is even, divide it by 2. 
If n is odd, multiply it by 3 and add 1. Repeat this process until n is 1. 
Write a recursive version of hailstone that prints out the values of 
the sequence and returns the number of steps.
'''
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of 
    elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    if n % 2 == 0:
        return 1 + hailstone(n // 2)
    elif n == 1:
        return 1
    else:
        return 1 + hailstone(3 * n + 1)
print(hailstone(10))


'''
Q5: Merge Numbers
Write a procedure merge(n1, n2) which takes numbers with digits in decreasing 
order and returns a single number with all of the digits of the two, 
in decreasing order. Any number merged with 0 will be that number 
(treat 0 as having no digits). Use recursion.

Hint: If you can figure out which number has the smallest digit out of both, 
then we know that the resulting number will have that smallest digit, 
followed by the merge of the two numbers with the smallest digit removed.
'''
def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    #find the smallest digit of both nubmer:
    if str(n1) + str(n2) <= '0':
        return None
    else:
        return  min(merge((str(n1) + str(n2)).replace(min(str(n1) + str(n2)),'')))

'''
Q6: Is Prime
Write a function is_prime that takes a single argument n and returns True 
if n is a prime number and False otherwise. Assume n > 1. 
We implemented this in Discussion 1 iteratively, now time to do it recursively!

Hint: You will need a helper function! Remember helper functions are nested 
functions that are useful if you need to keep track of more variables than 
the given parameters, or if you need to change the value of the input.
'''
def is_prime(n, j=2):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    if n <= 2:
        if n == 2:
            return True
        else:
            return False
    if n % j == 0:
        return False
    if j * j > n:
        return True
    else:
        return is_prime(n, j+1)
is_prime(521)