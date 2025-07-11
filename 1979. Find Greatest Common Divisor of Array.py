# https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

# Example 1:

# Input: nums = [2,5,6,9,10]
# Output: 2
# Explanation:
# The smallest number in nums is 2.
# The largest number in nums is 10.
# The greatest common divisor of 2 and 10 is 2.
nums = [4,5,7]
# --- My solution
class Solution:
    def findGCD(self, nums) -> int:
        a = max(nums)
        b = min(nums)
        while b:
            a, b = b, a %  b
        return a           
# --- Test 
sol = Solution()
print(sol.findGCD(nums))