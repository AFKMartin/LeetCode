# https://leetcode.com/problems/number-of-good-pairs/description
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
nums = [1,1,1,1]
# --- My solution
class Solution:
    def numIdenticalPairs(self, nums):
        res = 0
        f = {}
        for n in nums:
            res += f.get(n, 0)
            f[n] = f.get(n, 0) + 1
        return res

# --- Test
sol = Solution()
print(sol.numIdenticalPairs(nums))
