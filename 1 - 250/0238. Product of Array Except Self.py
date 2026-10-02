# https://leetcode.com/problems/product-of-array-except-self/description/ 
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
from typing import List
nums = [1,2,3,4]
# --- My Solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        one = 1
        for i in range(n):
            res[i] = one
            one *= nums[i]

        two = 1
        for i in range(n-1, -1, -1):
            res[i] *= two
            two *= nums[i]
        
        return res
    
# --- Test
sol = Solution()
print(sol.productExceptSelf(nums))