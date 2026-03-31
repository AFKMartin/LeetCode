# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

# Example 1:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# --- My solution   
class Solution:
    def luckyNumbers(self, matrix): 
        m, n = len(matrix), len(matrix[0])
        min_row = [min(row) for row in matrix]
        max_col = [max(matrix[i][j] for i in range(m)) for j in range(n)]

        return [matrix[i][j] for i in range(m) for j in range(n) if matrix[i][j] == min_row[i] == max_col[j]]   
# --- Test
sol = Solution()
print(sol.luckyNumbers(matrix))