# https://leetcode.com/problems/find-if-digit-game-can-be-won/description/
# You are given an array of positive integers nums.
# Alice and Bob are playing a game. In the game, Alice can choose either all single-digit numbers or all double-digit numbers from nums, and the rest of the numbers are given to Bob. Alice wins if the sum of her numbers is strictly greater than the sum of Bob's numbers.
# Return true if Alice can win this game, otherwise, return false.

# Example 1:

# Input: nums = [1,2,3,4,10]
# Output: false
# Explanation:
# Alice cannot win by choosing either single-digit or double-digit numbers.
nums = [5, 5, 5, 10, 10]
# --- My solution
class Solution:
    def canAliceWin(self, nums):
        c1 = sum(n for n in nums if n < 10)
        c2 = sum(n for n in nums if n > 9)
        return c1 != c2
# --- Test
sol = Solution()
print(sol.canAliceWin(nums))