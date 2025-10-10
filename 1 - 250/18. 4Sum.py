# https://leetcode.com/problems/4sum/description/
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
nums = [1,0,-1,0,-2,2]
target = 0 
# --- My solution
class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()  # Sort the array
        n = len(nums)
        res = []

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:  # Avoid duplicates on i
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]: # Avoid duplicates on j
                    continue
                left, right = j+1, n-1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                         # Avoid duplicates left and right
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res
# --- Test
sol = Solution()
print(sol.fourSum(nums, target))