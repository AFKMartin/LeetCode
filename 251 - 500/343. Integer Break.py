# https://leetcode.com/problems/integer-break/description
# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
# Return the maximum product you can get.

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
n = 100
# --- My solution
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1 # Edge cases: when 2 or 3 the solutions are 1 and 2
        if n == 3: return 2
        s = n // 3 
        if n % 3 == 0: # Case 1: for example 9, for any number n % 3 == 0, the optimal growth will be 3 ** (9//3)
            return 3 ** s

        if n % 3 == 1: # Case 2: for example 10, for any number n % 3 == 1, the optimal growth will be 3 ** (10//3 - 1) * 4
            return 3 ** (s-1) * 4 
        
        if n % 3 == 2: # Case 3: for example 11, for any number n % 3 == 2, the optimal growth will be 3 ** (11//3) * 2
            return 3 ** s * 2

# --- Test
sol = Solution()
print(sol.integerBreak(n))