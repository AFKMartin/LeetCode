# https://leetcode.com/problems/perfect-rectangle/description
# Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and the top-right point of it is (ai, bi).
# Return true if all the rectangles together form an exact cover of a rectangular region.
 
# Example 1:

# Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
# Output: true
# Explanation: All 5 rectangles together form an exact cover of a rectangular region.
rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
# --- My solution
class Solution:
    def isRectangleCover(self, rectangles):
        area = 0
        corners = set()

        min_x = min_y = float('inf')
        max_a = max_b = float('-inf')

        for x, y, a, b in rectangles:
            min_x, min_y = min(min_x, x), min(min_y, y)
            max_a, max_b = max(max_a, a), max(max_b, b)
            area += (a - x) * (b - y)

            for corner in [(x, y), (x, b), (a, y), (a, b)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)

        bounding_area = (max_a - min_x) * (max_b - min_y)
        if area != bounding_area:
            return False

        expected_corners = {
            (min_x, min_y), (min_x, max_b),
            (max_a, min_y), (max_a, max_b)
        }
        return corners == expected_corners

# --- Test
sol = Solution()
print(sol.isRectangleCover(rectangles))