# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
haystack = "sadbutsad"
needle = "sad"
# --- My Solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return - 1
        
# --- Test
sol = Solution()
print(sol.strStr(haystack, needle))