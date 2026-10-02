# https://leetcode.com/problems/excel-sheet-column-title/description
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 
# Example 1:
# Input: columnNumber = 1
# Output: "A"
columnNumber = 1
# --- My solution
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        c = ""
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            c += chr(ord("A") + rem)
            columnNumber //= 26
        
        return c[::-1]

# --- Test
sol = Solution()
print(sol.convertToTitle(columnNumber))
