# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
# Implement a function signFunc(x) that returns:
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
# Return signFunc(product).
# Example 1:
# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144) = 1
nums = [-1,-2,-3,-4,3,2,1]
# --- My solution
class Solution:
    def arraySign(self, nums):
        if 0 in nums:
            return 0
        return 1 if sum(num < 0 for num in nums) % 2 == 0 else -1

# --- Test
sol = Solution()
print(sol.arraySign(nums))