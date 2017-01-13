"""
Problem:

    Given a list of nums, find out whether the first and last items in the list
    are the same. If they are the same, print "Same"; if not, print "Different".
    If the list is empty, print "Empty"

Tests:

    >>> same_ends([1, 2, 3, 2, 1])
    Same
    >>> same_ends([2, 4, 5, 4])
    Different
    >>> same_ends([1])
    Same
    >>> same_ends([])
    Empty

"""

# This code tests your solution. Don't edit it. 
import doctest 
def run_tests(): 
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE) 


def same_ends(nums):



    if len(nums) == 0:
        print("Empty")

    elif nums[0] == nums[-1]:
        print("Same")


    else:
        print("Different")
        


