# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description
# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums. 
# Note: Subsets with the same elements should be counted multiple times.
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

# Example 1:

# Input: nums = [1,3]
# Output: 6
# Explanation: The 4 subsets of [1,3] are:
# - The empty subset has an XOR total of 0.
# - [1] has an XOR total of 1.
# - [3] has an XOR total of 3.
# - [1,3] has an XOR total of 1 XOR 3 = 2.
# 0 + 1 + 3 + 2 = 6
nums = [1,3]
# --- My solution
class Solution:
    def subsetXORSum(self, nums):
        res = 0
        for n in nums:
            res |= n
        return res * (1 << (len(nums) - 1))
# --- Test
sol = Solution()
print(sol.subsetXORSum(nums))