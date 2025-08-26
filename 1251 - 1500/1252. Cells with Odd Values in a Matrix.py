# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/description
# There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.
# For each location indices[i], do both of the following:
# Increment all the cells on row ri.
# Increment all the cells on column ci.
# Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.
# Example 1:

# Input: m = 2, n = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.
m = 2
n = 3
indices = [[0,1],[1,1]]
# --- My solution
class Solution:
    def oddCells(self, m: int, n: int, indices) -> int:
        row = [0] * m
        col = [0] * n

        for r,c in indices:
            row[r] += 1
            col[c] += 1

        c = 0
        for i in range(m):
            for j in range(n):
                if (row[i] + col[j]) % 2 == 1:
                    c += 1
        return c

# --- Test
sol = Solution()
print(sol.oddCells(m, n, indices))