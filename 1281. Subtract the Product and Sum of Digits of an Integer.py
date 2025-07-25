# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
n = 234
# --- My solution
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        dig = [int(d) for d in str(n)]
        prod = 1
        for d in dig:
            prod *= d
        return (prod - sum(dig))

# --- Test
sol = Solution()
print(sol.subtractProductAndSum(n))