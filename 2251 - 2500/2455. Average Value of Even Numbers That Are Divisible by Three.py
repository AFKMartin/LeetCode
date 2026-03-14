# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description
# Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.
# Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

# Example 1:

# Input: nums = [1,3,6,10,12,15]
# Output: 9
# Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.
nums = [1,2,4,7,10]
# --- My solution
class Solution:
    def averageValue(self, nums):
        c = []
        for n in nums:
            if n % 2 == 0 and n % 3 == 0:
                c.append(n)
        
        if len(c) == 0:
            return 0
        
        total = sum(c)
        return total // len(c)
    
# --- Test
sol = Solution()
print(sol.averageValue(nums))