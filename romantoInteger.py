# CHALLENGE: Roman to Integer
# DIFFICULTY: Easy
#===================================================================================
# Given a roman numeral, convert it to an integer.
#===================================================================================

class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        switch = 0
        rom = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        for digit in s[::-1]:
            if switch > rom[digit]:
                num -= rom[digit]
            else:
                num += rom[digit]
            switch = rom[digit]
        return num
