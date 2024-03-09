#CHALLENGE:
#===================================================================================
# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return
# the minimum integer common to both arrays. If there is no common integer amongst
# nums1 and nums2, return -1.

# Note that an integer is said to be common to nums1 and nums2 if both arrays have
# at least one occurrence of that integer.
#===================================================================================

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[0] > nums2[-1] or nums2[0] > nums1[-1]:
            return -1
        
        if nums1[0] > nums2[0]:
            for num in nums1:
                if num in nums2:
                    return num

        else:
            for num in nums2:
                if num in nums1:
                    return num
        return -1
