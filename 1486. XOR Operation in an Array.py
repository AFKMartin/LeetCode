# https://leetcode.com/problems/xor-operation-in-an-array/description/
# You are given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

# Example 1:

# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
# Where "^" corresponds to bitwise XOR operator.
n = 5
start = 0
# --- My solution
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        c = [start + 2*i for i in range(n)]
        res = 0
        for num in c:
            res ^= num
        return res

# --- Test 
sol = Solution()
print(sol.xorOperation(n, start))