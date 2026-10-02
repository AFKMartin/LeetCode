# https://leetcode.com/problems/contains-duplicate-ii/description/
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
nums = [-1,1,2,1]
k = 3
# --- My solution
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        c = {}
        for i, n in enumerate(nums):
            if n in c and i - c[n] <= k:
                return True
            c[n] = i
        return False 

# --- Test
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))