# CHALLENGE: Search Insert Position
# DIFFICULTY: Easy
#===================================================================================
# Given a sorted array of distinct integers and a target value, return the index if
# the target is found. If not, return the index where it would be if it were
# inserted in order.

# You must write an algorithm with O(log n) runtime complexity.
#===================================================================================

#Solution 1:
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

#Solution 2:
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        try:
            while nums[i] < target:
                i += 1
            return i
        except:
            return len(nums)
