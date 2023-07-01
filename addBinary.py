# CHALLENGE: Add Binary
# DIFFICULTY: Easy
#===================================================================================
# Given two binary strings a and b, return their sum as a binary string.
#===================================================================================

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        strs = [a, b]
        tot = 0
        for s in strs:
            i = 0
            for e in reversed(range(len(s))):
                if s[i] == '1':
                    tot += 2**e
                i += 1
        if tot == 0:
            return '0'
        start = 0
        j = 0
        bi = ''
        while start < tot:
            start += 2**j
            j+=1
        for k in reversed(range(j)):
            if 2**k <= tot:
                tot -= 2**k
                bi += '1'
            else:
                bi += '0'
        return bi
