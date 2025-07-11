# https://leetcode.com/problems/smallest-even-multiple/description/
# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
# Example 1:

# Input: n = 5
# Output: 10
# Explanation: The smallest multiple of both 5 and 2 is 10.
n = 5
# --- My solution
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return 2*n
# --- Test
sol = Solution()
print(sol.smallestEvenMultiple(n))