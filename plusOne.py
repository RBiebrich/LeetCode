# CHALLENGE: Plus One
# DIFFICULTY: Easy
#===================================================================================
# You are given a large integer represented as an integer array digits, where each
# digits[i] is the ith digit of the integer. The digits are ordered from most 
# significant to least significant in left-to-right order. The large integer does
# not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.
#===================================================================================

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
                if i-1 == -1:
                    digits.insert(0, 1)
            else:
                digits[i] += 1
                return digits
        return digits

#reverse and find first non-9 digit, work from there
