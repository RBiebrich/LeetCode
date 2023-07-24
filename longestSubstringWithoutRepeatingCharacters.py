# CHALLENGE: Longest Substring Without Repeating Characters
# DIFFICULTY: Medium
#===================================================================================
# Given a string s, find the length of the longest substring without repeating
# characters.
#===================================================================================

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        count = 0
        for char in s:
            if char in stack:
                stack = stack[stack.index(char)+1:]
            stack.append(char)
            if len(stack) > count:
                count = len(stack)
        
        return count
