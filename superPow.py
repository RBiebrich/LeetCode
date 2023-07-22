# CHALLENGE: Super Pow
# DIFFICULTY: Medium
#===================================================================================
# Your task is to calculate ab mod 1337 where a is a positive integer and b is an
# extremely large positive integer given in the form of an array.
#===================================================================================

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int(''.join(map(str, b))), 1337)
