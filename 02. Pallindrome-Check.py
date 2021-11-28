# Leetcode 9. Palindrome Number

"""
Input: x = 121
Output: true

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        x = str(x)
        rev_x = x[::-1]
        
        return x == rev_x


if __name__ == "__main__":
    x = 121
    print(x)
    print(Solution().isPalindrome(x))

    x = -121
    print(x)
    print(Solution().isPalindrome(x))
        