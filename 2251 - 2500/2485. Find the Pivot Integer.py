# https://leetcode.com/problems/find-the-pivot-integer/description
# Given a positive integer n, find the pivot integer x such that:
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.
 
# Example 1:

# Input: n = 8
# Output: 6
# Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
n = 8
# --- My solution
import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        res = n * (n + 1) // 2
        sqr = math.isqrt(res)

        if sqr * sqr == res:
            return sqr
        else:
            return -1 
# --- Test
sol = Solution()
print(sol.pivotInteger(n))