class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        unique_chars = set()
        res = 0
        for right in range(len(s)):
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left +=1
            unique_chars.add(s[right])
            res = max(res,right - left + 1)
        return res
            