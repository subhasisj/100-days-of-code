class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count_t,window = {},{}
        
        for c in t:
            count_t[c] = 1 + count_t.get(c,0)
            
        have,need = 0, len(count_t)
        res =  [-1,-1] # Default offsets for resulting substring
        reslen = float("infinity") # Take a large number to compare and find minimum
        
        l=0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            
            if s[r] in count_t and window[s[r]] == count_t[s[r]]: # if a char is in count_t, and the count is the same across both dictionaries increment have 
                have += 1
                
            while have == need:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = (r-l+1)
                # Pop elements from the left to make it minimum len
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:# If after removing from left we have broken have == need then 
                                                                    # we need to increase left and decrease have
                        have -=1
                l += 1
        l,r = res
        return s[l:r+1] if reslen !=float("infinity") else ""