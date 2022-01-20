class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0
        for i in range(len(s)):
            # If pallindrome is odd length then char before and after the middle char is the same
            l = r = i
            while (l >= 0 and r < len(s) and (s[l] == s[r])):
                if (r-l+1) > max_len:
                    max_len = r - l + 1
                    res = s[l:r+1]
                
                l-=1
                r+=1
            # In case the pallidrome is even
            l = i
            r = i+1
            while (l >= 0 and r < len(s) and (s[l] == s[r])):
                
                if (r-l+1) > max_len:
                    max_len = r - l + 1
                    res = s[l:r+1]
                l-=1
                r+=1
        return res
                
                   