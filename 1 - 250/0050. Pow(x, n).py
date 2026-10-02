# https://leetcode.com/problems/powx-n/description
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000

x = 2.00000
n = 10
# --- My solution
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return float(x ** n)
# --- Test
sol = Solution()
print(sol.myPow(x, n))