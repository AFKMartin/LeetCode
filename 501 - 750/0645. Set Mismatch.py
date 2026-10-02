# https://leetcode.com/problems/set-mismatch/description/
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
nums = [1,2,3,4,5,6,7,8,9,10,10,11]
# --- My solution
class Solution:
    def findErrorNums(self, nums):
        seen = set()
        c = 69 # haha 69, doesnt matter this intial value actually

        for n in nums:
            if n in seen:
                c = n
            seen.add(n) # all uniques values in nums

        n = len(nums) 
        miss = (set(range(1, n + 1)) - seen).pop() # From the correct set, remove every value in the incorrect set so you get the missing value

        return [c, miss]
        
# --- Test
sol = Solution()
print(sol.findErrorNums(nums))