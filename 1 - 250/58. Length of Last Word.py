# https://leetcode.com/problems/length-of-last-word/description/
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
s = "Hellow world"
# --- My solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_s = s.split()[-1]
        return len(last_s)

# --- Test
sol = Solution()
print(sol.lengthOfLastWord(s))