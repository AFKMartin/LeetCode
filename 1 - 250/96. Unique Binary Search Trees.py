# https://leetcode.com/problems/unique-binary-search-trees/description
# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
# Example 1:

# Input: n = 3
# Output: 5
n = 19
# --- My solution
import math
class Solution:
    def numTrees(self, n: int) -> int:
        fact = (math.factorial(2*n))/(math.factorial(n)*(math.factorial(n)))
        c = (1/(n+1))*fact
        return int(c)
# --- Test
sol = Solution()
print(sol.numTrees(n))