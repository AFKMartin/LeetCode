# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/description
# You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:
# The digit sum of n (the sum of its digits).
# The digit product of n (the product of its digits).
# Return true if n is divisible by this sum; otherwise, return false.
# Example 1:

# Input: n = 99
# Output: true
# Explanation:

# Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.
n = 99
# --- My solution
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sumd = 0
        prod = 1
        for d in str(n):
            digit = int(d)
            sumd += digit
            prod *= digit
        return n % (prod + sumd) == 0

# --- Test
sol = Solution()
print(sol.checkDivisibility(n))