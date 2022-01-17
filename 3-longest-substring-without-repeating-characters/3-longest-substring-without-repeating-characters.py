class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        longest_start_end = [0,1] # We take it as the first character
        start_idx = 0
        for i,c in enumerate(s):
            if c in last_seen:
                start_idx = max(start_idx,last_seen[c] + 1)
            if longest_start_end[1] - longest_start_end[0] <  (i + 1) - start_idx:
                longest_start_end = [start_idx, i + 1]
            last_seen[c] = i
                
        return len(s[longest_start_end[0]:longest_start_end[1]])
                