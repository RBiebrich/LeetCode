# CHALLENGE: Add to Array Form of Int
# DIFFICULTY: Easy
#===================================================================================
# The array-form of an integer num is an array representing its digits in left to 
# right order.

# For example, for num = 1321, the array form is [1,3,2,1].

# Given num, the array-form of an integer, and an integer k, return the array-form 
# of the integer num + k.
#===================================================================================


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = ''
        for n in num:
            s += str(n)
        tot = int(s) + k
        arr = []
        for m in str(tot):
            arr += [int(m)]
        return arr
