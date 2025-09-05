# https://leetcode.com/problems/rotate-array/description
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
nums = [1,2,3,4,5,6,7]
k = 100
# --- My solution
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l  # normalize k in case it's larger than l
        # nums[-k:] gives the last k elements (to move to the front)
        # nums[:-k] gives the first l-k elements (to follow after)
        # nums[:] ensures we modify the original list in place
        nums[:] = nums[-k:] + nums[:-k] 
# --- Test
        print(nums)
sol = Solution()
sol.rotate(nums, k)
