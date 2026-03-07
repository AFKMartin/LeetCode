# https://leetcode.com/problems/determine-color-of-a-chessboard-square/description
# You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.
# Return true if the square is white, and false if the square is black.
# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

# Example 1:

# Input: coordinates = "a1"
# Output: false
# Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
coordinates = "h3"
# --- My solution
class Solution:
    def squareIsWhite(self, coordinates):
        x = ord(coordinates[0]) - ord("a") + 1
        y = int(coordinates[1])
        
        return(x + y) % 2 == 1

# --- Test
sol = Solution()
print(sol.squareIsWhite(coordinates))