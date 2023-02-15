#CHALLENGE:
#===================================================================================
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
#
#An input string is valid if:
#
#    1. Open brackets must be closed by the same type of brackets.
#    2. Open brackets must be closed in the correct order.
#    3. Every close bracket has a corresponding open bracket of the same type.
#===================================================================================


class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []

        for char in s:
            if char in chars.keys(): # if the char is a key in the above dict, "chars"
                stack.append(chars[char]) # then append its paired value to the top of the stack
            elif not stack or char != stack[-1]: # if the above criteria are not met and if the stack is empty or the last thing in the stack is not the current char
                return False # then return False
            else: # if none of the above criteria are met, remove last thing in stack
                stack.pop()
                
        # this process/ the use of a stack ensures that all open chars are closed in the correct order
        # (or that failure to do so results in a False return)
        
        return len(stack) == 0
