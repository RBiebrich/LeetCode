# CHALLENGE: Single Number
# DIFFICULTY: Easy
#===================================================================================
# Given a non-empty array of integers nums, every element appears twice except for
# one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
#===================================================================================

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in set(nums):
            if nums.count(num) == 1:
                return num
