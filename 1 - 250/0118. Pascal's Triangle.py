# https://leetcode.com/problems/pascals-pascal/description/
# Given an integer numRows, return the first numRows of Pascal's pascal.
# In Pascal's pascal, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
numRows = 5
# --- My solution
class Solution:
    def generate(self, numRows: int):
        pascal = []
        for n in range(numRows):
            row = [1]  
            val = 1
            for k in range(1, n + 1):
                val = val * (n - k + 1) // k  
                row.append(val)
            pascal.append(row)
        
        return pascal
# --- Test
sol = Solution()
print(sol.generate(numRows))