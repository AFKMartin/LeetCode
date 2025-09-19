# https://leetcode.com/problems/count-numbers-with-unique-digits/description
# Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10**n.
# 0 <= n <= 8
# Example 1:

# Input: n = 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
n = 3
# --- My solution
# import math
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1 # edge case
        
        total = 10  # for n = 1
        first = 9  # first digit options (1-9)
        next = 9
        
        for i in range(2, n + 1):
            first *= next
            total += first
            next -= 1
        
        return total

# --- Test
sol = Solution()
print(sol.countNumbersWithUniqueDigits(n))