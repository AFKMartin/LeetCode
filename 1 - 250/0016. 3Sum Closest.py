# https://leetcode.com/problems/3sum-closest/description/
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
 
# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
nums = [-1,2,1,-4]
target = 1
# --- My solution
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        res = float("inf")
        k = len(nums)

        for i in range(k - 2):
            l, r = i + 1, k - 1
            while l < r:
                current = nums[i] + nums[l] + nums[r]

                # update closer to the target
                if abs(target - current) < abs(target - res):
                    res = current

                if current < target:
                    l += 1
                elif current > target:
                    r -= 1
                
                else:
                    # exact match
                    return current
        # if not exact match at current
        return res



        
# --- Test
sol = Solution()
print(sol.threeSumClosest(nums, target))