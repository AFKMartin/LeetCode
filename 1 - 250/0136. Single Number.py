# https://leetcode.com/problems/single-number/description/
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1
nums = [2,2,1]
# --- My solution
class Solution:
    def singleNumber(self, nums) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res
# --- Test
sol = Solution()
print(sol.singleNumber(nums))