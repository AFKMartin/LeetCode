# https://leetcode.com/problems/number-of-common-factors/description/
# Given two positive integers a and b, return the number of common factors of a and b.
# An integer x is a common factor of a and b if x divides both a and b.

# Example 1:

# Input: a = 12, b = 6
# Output: 4
# Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
a = 30
b = 25
# --- My solution
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        def gcd(a, b):
            while b:
                a , b = b, a % b
            return a
        g = gcd(a,b)
        return len([i for i in range(1, g + 1) if g % i == 0])
# --- Test
sol = Solution()
print(sol.commonFactors(a,b))