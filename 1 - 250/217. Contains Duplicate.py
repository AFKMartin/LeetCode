# https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.
nums = [1,2,3,1]
nums2 = [1,2,3,4]
# --- My Solution
class Solution:
    def containsDuplicate(self, nums) -> bool:
        hs = set() 

        for n in nums:           
            if n in hs:          
                return True      
            hs.add(n)            
        return False             
# --- My test
sol = Solution()
print(sol.containsDuplicate(nums))
print(sol.containsDuplicate(nums2))


