class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts_t = {}
        counts_s = {}
        for i in range(len(s)):
            counts_t[t[i]] = 1 + counts_t.get(t[i],0)
            counts_s[s[i]] = 1 + counts_s.get(s[i],0)
        return counts_t == counts_s
               