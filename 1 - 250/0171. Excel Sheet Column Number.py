# https://leetcode.com/problems/excel-sheet-column-number/description
# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
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

# Input: columnTitle = "A"
# Output: 1
columnTitle = "A"
# --- My solution
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        c = 0
        for char in columnTitle:
            c = c * 26 + (ord(char) - ord("A") + 1)
        return c

# --- Test
sol = Solution()
print(sol.titleToNumber(columnTitle))