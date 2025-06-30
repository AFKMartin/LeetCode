# https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
# Given an integer num, return the number of digits in num that divide num.
# An integer val divides nums if nums % val == 0.

# Example 1:

# Input: num = 7
# Output: 1
# Explanation: 7 divides itself, hence the answer is 1.
num = 122
# --- My solution
class Solution:
    def countDigits(self, num: int) -> int:
        return sum(1 for d in str(num) if d != "0" and num % int(d) == 0)
# --- Test
sol = Solution()
print(sol.countDigits(num))

