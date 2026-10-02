# https://leetcode.com/problems/power-of-two/description/
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2^x.

# Example 1:

# Input: n = 1
# Output: true

# Explanation: 2^0 = 1
n = 15
# --- My solution
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        return True if n > 0 and (n & (n - 1)) == 0 else False
        
# --- Test
sol = Solution()
print(sol.isPowerOfTwo(n))