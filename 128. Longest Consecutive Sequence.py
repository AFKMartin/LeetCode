# https://leetcode.com/problems/longest-consecutive-sequence/
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3
from typing import List
# --- My solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        long = 0
        for num in numset:
            if num - 1 not in numset:
                current = num
                length = 1

                while current + 1 in numset:
                    current +=1
                    length += 1

                long = max(long, length)
        return long   
# --- Test 
sol = Solution()
print(sol.longestConsecutive([1000, 1001, 1002, 1003, 1, 2, 3]))