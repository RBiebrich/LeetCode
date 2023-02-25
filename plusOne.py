#CHALLENGE:
#===================================================================================
# You are given a large integer represented as an integer array digits, where each
# digits[i] is the ith digit of the integer. The digits are ordered from most
# significant to least significant in left-to-right order. The large integer does not
# contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.
#===================================================================================

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if set(digits) == {9}:
            digits.insert(0, 0)
        for i, digit in list(enumerate(digits))[::-1]:
            if digit == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        return digits

#reverse and find first non-9 digit, work from there
