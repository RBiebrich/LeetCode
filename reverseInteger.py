
#CHALLENGE:
#===================================================================================
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x
# causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
# then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
#===================================================================================


class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            x = int((x**2)**(1/2))
            out = 0 - int(str(x)[::-1])
        else:
            out = int(str(x)[::-1])
        if out > (2**31)-1 or out < -(2**31):
            return 0
        else:
            return out
