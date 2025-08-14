# https://leetcode.com/problems/surface-area-of-3d-shapes/description
# You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).
# After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.
# Return the total surface area of the resulting shapes.
# Note: The bottom face of each shape counts toward its surface area.

# Example 1:

# Input: grid = [[1,2],[3,4]]
# Output: 34
grid = [[1,2],[3,4]]
# --- My solution
class Solution:
    def surfaceArea(self, grid) -> int:
        c = 0
        n = len(grid)

        for i in range(n):
            for j in range(n):
                h = grid[i][j]
                # top and bot
                if h > 0:
                    c += 2
                
                # sides
                # up
                if i == 0:
                    c += h
                else:
                    c += max(h - grid[i-1][j], 0)
                
                # Down
                if i == n-1:
                    c += h
                else:
                    c += max(h - grid[i+1][j], 0)
                
                # left
                if j == 0:
                    c += h
                else:
                    c += max(h - grid[i][j-1], 0)
                
                # right
                if j == n-1:
                    c += h
                else:
                    c += max(h - grid[i][j+1], 0)
        return c

# --- Test
sol = Solution()
print(sol.surfaceArea(grid))