#CHALLENGE:
#===================================================================================
#Given an array of integers nums and an integer target, return indices of the two 
#numbers such that they add up to target. You may assume that each input would have 
#exactly one solution, and you may not use the same element twice. You can return 
#the answer in any order.
#===================================================================================


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in enumerate(nums):
            dif = target - j
            if dif in nums and nums.index(dif) != i:
                ans = [i, nums.index(dif)]
        return ans
