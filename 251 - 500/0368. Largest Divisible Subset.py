# https://leetcode.com/problems/largest-divisible-subset/description
# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.
nums = [1,2,3]
# --- My solution
class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        
        # dp[i] = length of largest subset ending with nums[i]
        dp = [1] * n
        parent = [-1] * n  # to rebuildpath
        
        max_len = 1
        max_idx = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i
        
        # rebuild subset
        result = []
        while max_idx != -1:
            result.append(nums[max_idx])
            max_idx = parent[max_idx]
        
        return result[::-1]  # reverse to start from smallest
# --- Test
sol = Solution()
print(sol.largestDivisibleSubset(nums))