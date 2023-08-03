# CHALLENGE: Move Zeroes
# DIFFICULTY: Easy
#===================================================================================
# Given an integer array nums, move all 0's to the end of it while maintaining the
# relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
#===================================================================================

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        off = 0
        for i in range(len(nums)):
            if nums[i-off] == 0:
                nums.pop(i-off)
                nums.append(0)
                off += 1
