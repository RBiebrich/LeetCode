# CHALLENGE: Find the Index of the First Occurrence in a String
# DIFFICULTY: Easy
#===================================================================================
# Given two strings needle and haystack, return the index of the first occurrence of
# needle in haystack, or -1 if needle is not part of haystack.
#===================================================================================

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[start:start+len(needle)] == needle:
                return start
            else:
                start += 1
        return -1
