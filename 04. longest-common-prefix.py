"""
Leetcode 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from typing import List


class Solution:
    # runtime: O(n^2)
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        # Loop through all chars of the first string
        # and compare it with the char in same position in the other strings
        for i in range(len(strs[0])):
            for s in strs:
                if (
                    i == len(s) or s[i] != strs[0][i]
                ):  # The first condition checks for i being out of bounds when s is shorter than strs[0]
                    return res
            res += strs[0][i]

        return res


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(strs)
    print(Solution().longestCommonPrefix(strs))

    strs = ["dog", "racecar", "car"]
    print(strs)
    print(Solution().longestCommonPrefix(strs))

    strs = [""]
    print(strs)
    print(Solution().longestCommonPrefix(strs))
