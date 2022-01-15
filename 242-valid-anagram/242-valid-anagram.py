class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts_t = {}
        counts_s = {}
        for i in range(len(s)):
            if t[i] in counts_t:
                counts_t[t[i]]+=1
            else:
                counts_t[t[i]] = 1
            if s[i] in counts_s:
                counts_s[s[i]]+=1
            else:
                counts_s[s[i]] = 1
        return counts_t == counts_s
               