# https://leetcode.com/problems/projection-area-of-3d-shapes/description
# You are given an n x n grid where we place some 1 x 1 x 1 cubes that are axis-aligned with the x, y, and z axes.
# Each value v = grid[i][j] represents a tower of v cubes placed on top of the cell (i, j).
# We view the projection of these cubes onto the xy, yz, and zx planes.
# A projection is like a shadow, that maps our 3-dimensional figure to a 2-dimensional plane. We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
# Return the total area of all three projections.

# Example 1:

# Input: grid = [[1,2],[3,4]]
# Output: 17
# Explanation: Here are the three projections ("shadows") of the shape made with each axis-aligned plane.
grid = [[1,2],[3,4]]
# --- My solution
class Solution:
    def projectionArea(self, grid) -> int:
        c = 0
        # top
        for sub in grid:
            for i in range(len(sub)):
                if sub[i] != 0:
                    c += 1
        # front
        for sub in grid:
            c += max(sub)
        # side
        for j in range(len(sub)):
            col = 0
            for i in range(len(sub)):
                col = max(col, grid[i][j])
            c += col
        return c

# --- Test
sol = Solution()
print(sol.projectionArea(grid))