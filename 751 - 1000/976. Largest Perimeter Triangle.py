# https://leetcode.com/problems/largest-perimeter-triangle/description
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

# Example 1:

# Input: nums = [2,1,2]
# Output: 5
# Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
# 3 <= nums.length <= 104
# 1 <= nums[i] <= 106
nums = [2,1,2]
# --- My solution
class Solution:
    def largestPerimeter(self, nums) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if b + c > a:
                return a + b + c
        return 0

# --- Test
sol = Solution()
print(sol.largestPerimeter(nums))