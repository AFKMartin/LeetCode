# https://leetcode.com/problems/palindrome-number/description/
# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
x = 121
# --- My solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = str(x)
        return z == z[::-1]
# --- Test
sol = Solution()
print(sol.isPalindrome(x))