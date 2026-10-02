# https://leetcode.com/problems/arranging-coins/description
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.
# Example 1 is a image go check the link above.
# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
n = 5
# --- My solution
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (1 + 8*n)**0.5) // 2)
# --- Test
sol = Solution()
print(sol.arrangeCoins(n))