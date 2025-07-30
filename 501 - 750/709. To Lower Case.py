# https://leetcode.com/problems/to-lower-case/description/
# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
# 
# Example 1:
# 
# Input: s = "Hello"
# Output: "hello"

s = "HeLlO"
# --- My solution
class Solution:
    def toLowerCase(self, s: str) -> str:
        return (s.lower())
# --- Test
sol = Solution() 
print(sol.toLowerCase(s))