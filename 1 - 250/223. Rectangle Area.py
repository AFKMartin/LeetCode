# https://leetcode.com/problems/rectangle-area/description
# Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
# The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).
# The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

# Example 1:

# Rectangle Area
# Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
# Output: 45
ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2
# --- My solution
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Working on this
# --- Test
sol = Solution()
print(sol.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))
