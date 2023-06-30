# CHALLENGE: Longest Common Prefix
# DIFFICULTY: Easy
#===================================================================================
# Write a function to find the longest common prefix string amongst an array of
# strings.

# If there is no common prefix, return an empty string "".
#===================================================================================

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        prefix = ""
        for let in strs[0]:
            for word in strs[1:]:
                if not word.startswith(prefix + let):
                    return prefix
            prefix += let
        return prefix
