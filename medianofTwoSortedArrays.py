
# CHALLENGE: Median of Two Sorted Arrays
# DIFFICULTY: Hard
#===================================================================================
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the
# median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).
#===================================================================================

# My most effiecent solution:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1+nums2)
        length = len(nums)
        if length%2 == 0:
            return sum(nums[int(length/2-1):int(length/2+1)])/2
        else:
            return nums[int(length/2)]

# My least efficient solution, but neat use of while loop:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        while len(nums)>2:
            nums.pop(0)
            nums.pop(-1)
        return (sum(nums)/len(nums))
