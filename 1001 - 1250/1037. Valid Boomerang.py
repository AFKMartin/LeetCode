# https://leetcode.com/problems/valid-boomerang/description
# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.
# A boomerang is a set of three points that are all distinct and not in a straight line.
# Example 1:

# Input: points = [[1,1],[2,3],[3,2]]
# Output: true
points = [[1,1],[2,3],[3,2]]
# --- My solution
class Solution:
    def isBoomerang(self, points) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points
        
        if len({(x1, y1), (x2, y2), (x3, y3)}) < 3:
            return False
        
        return (y3 - y1) * (x2 - x1) != (y2 - y1) * (x3 - x1)
# --- Test
sol = Solution()
print(sol.isBoomerang(points))