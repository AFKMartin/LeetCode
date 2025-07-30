# https://leetcode.com/problems/two-sum/description/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
nums = [2,7,11,15]
target = 9
# --- My Solution
class Solution:
    def twoSum(self, nums, target):
        m = {} 
        for i, n in enumerate(nums): 
            d = target - n  
            if d in m: 
                return [m[d], i] 
            m[n] = i 
# --- Test
sol = Solution()
print(sol.twoSum(nums, target))

