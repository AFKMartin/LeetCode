# https://leetcode.com/problems/max-points-on-a-line/description
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
# Example 1:
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
points = [[1,1],[3,3],[2,2]]
# --- My solution
import math
from collections import defaultdict

class Solution:
    def maxPoints(self, points) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        res = 0

        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 0
            maximum = 0

            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                g = math.gcd(dx, dy)
                dx //= g
                dy //= g

                if dx == 0:      
                    dy = 1
                elif dy == 0:    
                    dx = 1
                elif dx < 0:     
                    dx, dy = -dx, -dy

                slopes[(dy, dx)] += 1
                maximum = max(maximum, slopes[(dy, dx)])

            res = max(res, maximum + duplicates + 1)

        return res


# --- Test
sol = Solution()
print(sol.maxPoints(points))