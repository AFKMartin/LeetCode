# https://leetcode.com/problems/missing-number/description/
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation:
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
nums = [0,1,2]
# --- My solution
class Solution:
    def missingNumber(self, nums) -> int:
        x = len(nums)
        y = x * (x + 1) // 2
        s = sum(nums)
        return y - s
     
# --- Test
sol = Solution()
print(sol.missingNumber(nums))