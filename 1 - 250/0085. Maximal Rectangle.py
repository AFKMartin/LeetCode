# https://leetcode.com/problems/maximal-rectangle/
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# Example 1:

# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# --- My solution
class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0]) 
        heights = [0] * cols 
        max_area = 0

        for row in matrix:
            for i in range(cols):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
        
            max_area = max(max_area, self.largestRectangleArea(heights))
    
        return max_area

    def largestRectangleArea(self, heights):
        s = []
        max_area = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while s and heights[s[-1]] > h:
                height = heights[s.pop()]
                width = i if not s else i - s[-1] - 1
                max_area = max(max_area, height * width)
            s.append(i)
        
        heights.pop()
        return max_area

# --- Test
sol = Solution()
print(sol.maximalRectangle(matrix))
