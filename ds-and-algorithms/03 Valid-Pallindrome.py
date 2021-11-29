"""
Leetcode 125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        alnum = "".join([i for i in s if i.isalnum() ])
        
        return alnum == alnum[::-1]
        

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(s)
    print(Solution().isPalindrome(s))

    s = "race a car"
    print(s)
    print(Solution().isPalindrome(s))

