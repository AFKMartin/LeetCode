# https://leetcode.com/problems/counting-bits/description/
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
n = 5
# --- My solution
class Solution:
    def countBits(self, n: int):
        return [bin(i).count("1") for i in range(n+1)] # count the numbers of 1 in each number and just return it listed
# --- Test
sol = Solution()
print(sol.countBits(n))