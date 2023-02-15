#CHALLENGE:
#===================================================================================
#Given an array nums. We define a running sum of an array as 
# runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.
#===================================================================================

class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):

            if i > 0:

                nums[i] = nums[i] + nums[i-1]

        return nums
