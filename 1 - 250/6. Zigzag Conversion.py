# https://leetcode.com/problems/zigzag-conversion/description/
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
s = "PAYPALISHIRING"
numRows = 3
# --- My solution
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        row = [""] * numRows
        cur_row = 0
        down = False

        for c in s:
            row[cur_row] += c

            if cur_row == 0 or cur_row == numRows - 1:
                down = not down
            
            cur_row += 1 if down else -1
        
        return "".join(row)

        
# --- Test
sol = Solution()
print(sol.convert(s, numRows))