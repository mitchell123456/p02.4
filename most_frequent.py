"""
Problem:

    Given a list of integers, nums, and two integers, a and b, we would like
    to find out which one occurs most frequently in our list.
    If either a or b appears more often, print that number.
    If neither appears at all, print "Neither".
    If they appear the same number of times, print "Tie".
    

Tests:

    >>> mode([1, 2, 3, 3], 2, 3)
    3
    >>> mode([1, 2, 2, 3, 4], 2, 3)
    2
    >>> mode([1, 2, 2, 1, 2], 3, 4)
    Neither
    >>> mode([2, 2, 3, 3], 2, 3)
    Tie
    >>> mode([], 1, 2)
    Neither

"""

# This code tests your solution. Don't edit it. 
import doctest 
def run_tests(): 
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE) 


def mode(nums, a, b):

    length = len(nums)
    a_count = 0
    b_count = 0

    for n in range(0, length):
        if a == nums[n]:
            a_count = a_count + 1

        if b == nums[n]:
            b_count = b_count + 1


    if a_count == 0 and b_count == 0:
        print("Neither")

    elif a_count > b_count:
        print(a)

    elif b_count > a_count:
        print(b)

    else:
        print("Tie")

