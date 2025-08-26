# https://leetcode.com/problems/check-if-it-is-a-straight-line/description
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# Example 1:

# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# --- My solution
class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        (x0, y0), (x1, y1) = coordinates[:2]
        val_y = (y1 - y0) 
        val_x = (x1 - x0)
        for x, y in coordinates[2:]:
            if val_y * (x - x0) != val_x * (y - y0): 
                return False
        return True
# --- Test
sol = Solution()
print(sol.checkStraightLine(coordinates))