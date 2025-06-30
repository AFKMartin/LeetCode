# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/
# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

# Example 1:

# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
words = ["abc","car","ada","racecar","cool"]
# --- My solution
class Solution:
    def firstPalindrome(self, words):
        return next((w for w in words if w == w[::-1]), "")
# --- Test
sol = Solution()
print(sol.firstPalindrome(words))

