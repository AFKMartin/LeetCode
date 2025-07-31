# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description
# You are given an integer array nums.
# Return the smallest index i such that the sum of the digits of nums[i] is equal to i.
# If no such index exists, return -1.

# Example 1:

# Input: nums = [1,3,2]
# Output: 2
# Explanation:
# For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.
nums = [1,3,2]
# --- My solution
class Solution:
    def smallestIndex(self, nums) -> int:
        for i in range(len(nums)):
            s = sum(int(d) for d in str(nums[i]))
            if s == i:
                return i
        return -1
# --- Test 
sol = Solution()
print(sol.smallestIndex(nums))