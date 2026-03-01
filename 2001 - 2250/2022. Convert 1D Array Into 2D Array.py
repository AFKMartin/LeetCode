# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/
# You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.
# The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.
# Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.

# Example 1:

# Input: original = [1,2,3,4], m = 2, n = 2
# Output: [[1,2],[3,4]]
# Explanation: The constructed 2D array should contain 2 rows and 2 columns.
# The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
# The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.
original = [1,2,3]
m = 1
n = 3
# --- My solution
class Solution:
    def construct2DArray(self, original, m, n):
        res = []
        if len(original) != m * n:
            return []
        else:
            for i in range(m):
                res.append(original[i*n:(i+1)*n])
        return res
# --- Test
sol = Solution()
print(sol.construct2DArray(original, m, n))