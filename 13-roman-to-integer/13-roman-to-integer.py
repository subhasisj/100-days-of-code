class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value =  {'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        value = 0
        for i in range(1,len(s)):
            if symbol_value[s[i-1]] < symbol_value[s[i]]:
                value -= symbol_value[s[i-1]]
            else:
                value += symbol_value[s[i-1]]
        value += symbol_value[s[-1]]
        return value
                
        