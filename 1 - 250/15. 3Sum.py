# https://leetcode.com/problems/3sum/description/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
nums = [-1,0,1,2,-1,-4]
# --- My solution
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                break

            left, right = i + 1, n -1

            while left < right:
                x = nums[i] + nums[left] + nums[right]

                if x == 0:
                    # here you found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                    left, right = left + 1, right -1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif x < 0:
                    left += 1
                
                else:
                    right -= 1
        return res


# --- Test
sol = Solution()
print(sol.threeSum(nums))