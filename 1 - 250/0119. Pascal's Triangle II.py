# https://leetcode.com/problems/pascals-triangle-ii/description/
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
rowIndex = 3
# --- My solution
class Solution:
    def getRow(self, rowIndex: int):
        x = rowIndex + 1
        pascal = []
        for n in range(x):
            row = [1]  
            val = 1
            for k in range(1, n + 1):
                val = val * (n - k + 1) // k  
                row.append(val)
            pascal.append(row)
        
        return pascal[rowIndex]
# --- Test
sol = Solution()
print(sol.getRow(rowIndex))