# https://leetcode.com/problems/maximum-product-of-three-numbers/description
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
nums = [1,2,3]
# --- My solution
class Solution:
    def maximumProduct(self, nums) -> int:
        x = sorted(nums)
        return max((x[-1] * x[-2] * x[-3]), (x[0] * x[1] * x[-1]))
    
# --- Test
sol = Solution()
print(sol.maximumProduct(nums))