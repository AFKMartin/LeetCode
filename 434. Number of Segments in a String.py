# https://leetcode.com/problems/number-of-segments-in-a-string/description/
# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.
# Example 1:

# Input: s = "Hello, my name is John"
# Output: 5
#Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
s = "Hello, my name is John"
# --- My Solution
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
# --- Test
sol = Solution()
print(sol.countSegments(s))