# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/description
# You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.
# The following proccess happens k times:
# Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.
# Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.
# Return true if the final modified matrix after k steps is identical to the original matrix, and false otherwise.

# Example 1:

# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4
# Output: false
# Explanation:
# In each step left shift is applied to rows 0 and 2 (even indices), and right shift to row 1 (odd index).
mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
k = 2
# --- My solution
class Solution:
    def areSimilar(self, mat, k):
        m, n = len(mat), len(mat[0])
        k %= n  # there was unnecessary rotations when k >= n

        for i in range(m):
            for j in range(n):
                src = (j + k) % n if i % 2 == 0 else (j - k) % n
                if mat[i][src] != mat[i][j]:
                    return False
        return True
# --- Test
sol = Solution()
print(sol.areSimilar(mat, k))