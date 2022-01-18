class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = {}
        l = 0
        res = 0
        for r in range(len(s)):
            char_counts[s[r]] = 1 + char_counts.get(s[r],0) # Return 0 count if a char is not existing in the dictionary
            while ((r - l + 1) - max(char_counts.values()) > k ): # if the length of sliding window - max char count is greater than
                                                                   # allowed replacement 
                    char_counts[s[l]] -= 1
                    l+=1
            res = max(res, r - l + 1)
        return res