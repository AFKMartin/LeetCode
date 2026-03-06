# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

# Example 1:

# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].
low = 8
high = 10
# --- My solution
class Solution:
    def countOdds(self, low, high):
        return (high + 1) // 2 - low // 2
# --- Test
sol = Solution()
print(sol.countOdds(low, high))