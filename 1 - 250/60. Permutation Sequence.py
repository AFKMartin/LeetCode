# https://leetcode.com/problems/permutation-sequence/description
# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Example 1:

# Input: n = 3, k = 3
# Output: "213"
n = 3
k = 3
# --- My solution
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [str(i) for i in range(1, n+1)]
        k -= 1
        res = []

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            res.append(digits.pop(index))
            k %= fact
        return "".join(res)
# --- Test
sol = Solution()
print(sol.getPermutation(n, k))