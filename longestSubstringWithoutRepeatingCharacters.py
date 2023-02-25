#CHALLENGE:
#===================================================================================
# Given a string s, find the length of the longest substring without repeating
# characters.
#===================================================================================

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        count = 0
        start = None
        for i, let in enumerate(s):
            for let in s[i:]:
                if let not in lst:
                    lst.append(let)
                    if len(lst) > count:
                        count = len(lst)
                else:
                    lst.clear()
                    break

        return count
