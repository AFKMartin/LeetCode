# https://leetcode.com/problems/self-crossing/description
# You are given an array of integers distance.
# You start at the point (0, 0) on an X-Y plane, and you move distance[0] meters to the north, then distance[1] meters to the west, distance[2] meters to the south, distance[3] meters to the east, and so on. In other words, after each move, your direction changes counter-clockwise.
# Return true if your path crosses itself or false if it does not.
# Example 1:

# Input: distance = [2,1,1,2]
# Output: true
# Explanation: The path crosses itself at the point (0, 1).
distance = [2,1,1,2]
# --- My solution
class Solution:
    def isSelfCrossing(self, distance) -> bool:
        d = distance
        for i in range(3, len(d)):
            # case 1 crossing
            if d[i] >= d[i-2] and d[i-1] <= d[i-3]:
                return True
            
            # case 2 overlap
            if i >= 4 and d[i-1] == d[i-3] and d[i] + d[i-4] >= d[i-2]:
                return True

            # case 3 spiral overlap
            if (i >= 5 and d[i-2] >= d[i-4] and d[i] + d[i-4] >= d[i-2] and d[i-1] <= d[i-3] and d[i-1] + d[i-5] >= d[i-3]):
                return True
            
        return False # anything outside these 3 cases will be false.
# --- Test
sol = Solution()
print(sol.isSelfCrossing(distance)) 