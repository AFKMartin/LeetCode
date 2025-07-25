# https://leetcode.com/problems/power-of-four/description
# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.

# Example 1:

# Input: n = 16
# Output: true
n = 16
# --- My solution
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 4 == 0:
            n = n // 4
        return n == 1        
# --- Test
sol = Solution()
print(sol.isPowerOfFour(n))