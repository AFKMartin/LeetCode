# https://leetcode.com/problems/valid-palindrome/description/
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
s = "A man, a plan, a canal: Panama"
# --- My solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = "".join(ch.lower() for ch in s if ch.isalnum())
        return x == x[::-1]
# --- Test
sol = Solution()
print(sol.isPalindrome(s))