# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to c the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

# Example 1:

# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
nums = [8,1,2,2,3]
# --- My solution
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        c = [0] * 501
        for n in nums:
            c[n] += 1

        prefix = [0] * 501
        for i in range(1, 501):
            prefix[i] = prefix[i-1] + c[i-1]

        res = [prefix[n] for n in nums] 
        return res

# --- Test
sol = Solution()
print(sol.smallerNumbersThanCurrent(nums))