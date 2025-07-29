# https://leetcode.com/problems/rectangle-overlap/description
# An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.
# Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.
# Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

# Example 1:

# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
# --- My solution
class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        # rec1 = [x1,y1,x2,y2]
        # rec2 = [x3,y3,x4,y4]
        # x1 < x4 and x3 > x2
        # y1 < y4 and y3 > y2
        return rec1[0] < rec2[2] and rec1[2] > rec2[0] and rec1[1] < rec2[3] and rec1[3] > rec2[1]


# --- Test
sol = Solution()
print(sol.isRectangleOverlap(rec1, rec2))