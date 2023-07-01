# CHALLENGE: Length of Last Word
# DIFFICULTY: Easy
#===================================================================================
# Given a string s consisting of words and spaces, return the length of the last
# word in the string.

# A word is a maximal substring consisting of non-space characters only.
#===================================================================================

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split()
        return len(lst[-1])
