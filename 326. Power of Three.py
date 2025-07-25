# https://leetcode.com/problems/power-of-three/description/
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33
n = 28
# --- My solution
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n = n // 3
        return n == 1
        
# --- Test
sol = Solution()
print(sol.isPowerOfThree(n))