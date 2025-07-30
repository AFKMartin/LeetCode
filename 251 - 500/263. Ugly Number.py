# https://leetcode.com/problems/ugly-number/description/
# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
n = 0
# --- My solution
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0:
            return False
        while n % 2 == 0:
            n = n // 2
        while n % 3 == 0:
            n = n // 3
        while n % 5 == 0:
            n = n // 5
        if n == 1:
            return True
        else:
            return False
# --- Test
sol = Solution()
print(sol.isUgly(n))