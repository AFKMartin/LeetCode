# https://leetcode.com/problems/add-digits/description/
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
# Example 1:
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
num = 9876
# --- My solution
class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else 1 + (num-1) % 9
# --- Test 
sol = Solution()
print(sol.addDigits(num))
