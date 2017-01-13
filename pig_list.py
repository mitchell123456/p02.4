"""
Problem:

    Given a list of integers, nums, the function `rotate` should move
    the first item in the list to the end, and then print it.
    If the list is empty, it should just print the empty list.

Tests:

    >>> rotate([1, 2, 3, 4])
    [2, 3, 4, 1]
    >>> rotate([5, 7, 9, 2, 1, 4])
    [7, 9, 2, 1, 4, 5]
    >>> rotate([2])
    [2]
    >>> rotate([])
    []

"""

# This code tests your solution. Don't edit it. 
import doctest 
def run_tests(): 
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE) 


def rotate(nums):

    if len(nums) == 1 or len(nums) == 0:
        print(nums)

    else:
        nums.insert(len(nums), nums[0])
        nums.remove(nums[0])
        print(nums)
