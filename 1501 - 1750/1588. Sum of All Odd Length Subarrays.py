# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description
# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
# A subarray is a contiguous subsequence of the array.

# Example 1:

# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
arr = [1,4,2,5,3]
# --- My solution
class Solution:
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        res = 0
        for i, num in enumerate(arr):
            subres = (i + 1) * (n - i)
            oddres = (subres + 1)//2
            res += num * oddres
        return res
# --- Test
sol = Solution()
print(sol.sumOddLengthSubarrays(arr))