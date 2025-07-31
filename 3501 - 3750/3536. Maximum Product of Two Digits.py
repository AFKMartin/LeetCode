# https://leetcode.com/problems/maximum-product-of-two-digits/description
# You are given a positive integer n.
# Return the maximum product of any two digits in n.
# Note: You may use the same digit twice if it appears more than once in n.

# Example 1:

# Input: n = 31
# Output: 3
# Explanation:
# The digits of n are [3, 1].
# The possible products of any two digits are: 3 * 1 = 3.
# The maximum product is 3.
n = 124
# --- My solution
class Solution:
    def maxProduct(self, n: int) -> int:
        c = []
        for d in str(n):
            c.append(d) 
        x = sorted(c, reverse=True)[:2]
        return int(x[0]) * int(x[1])
# --- Test
sol = Solution()
print(sol.maxProduct(n))