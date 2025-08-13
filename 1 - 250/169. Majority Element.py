# https://leetcode.com/problems/majority-element/description/
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
nums = [2,2,3,3,3]
# --- My solution
class Solution:
    def majorityElement(self, nums) -> int:
        # Boyer-Moore Voting Algorithm
        candidate = None
        c = 0
        for n in nums:
            if c == 0:
                candidate = n
                c = 1
            elif n == candidate:
                c += 1
            else:
                c -= 1
        return candidate

# --- Test
sol = Solution()
print(sol.majorityElement(nums))