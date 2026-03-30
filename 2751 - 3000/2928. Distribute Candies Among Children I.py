# https://leetcode.com/problems/distribute-candies-among-children-i/description
# You are given two positive integers n and limit.
# Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

# Example 1:

# Input: n = 5, limit = 2
# Output: 3
# Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).
n = 3
limit = 3
# --- My solution
from math import comb
class Solution:
    @staticmethod          
    def C2(k):
        return comb(k, 2) if k >= 2 else 0
    
    def distributeCandies(self, n, limit):
        return (
            self.C2(n + 2)
            - 3 * self.C2(n - limit + 1)
            + 3 * self.C2(n - 2 * limit)
            - self.C2(n - 3 * limit - 1)
        )       
# --- Test
sol = Solution()
print(sol.distributeCandies(n, limit))