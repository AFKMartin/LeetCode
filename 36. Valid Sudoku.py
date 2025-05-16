# https://leetcode.com/problems/valid-sudoku/description/ 
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# Example 1: https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png
# Input: 
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
# Output: true
from typing import List
# --- My solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)] # create a list of sets for storing rows
        cols = [set() for _ in range(9)] # same for cols
        boxes = {} # creates an empty dictionary "That's a Surprise Tool That Can Help us Later"

        for r in range(9): # loop 9 times, if needed based on value of r
            for c in range(9): # loop 9 times, if needed based on value of c
                val = board[r][c] # val takes each cell value from the board as we iterate rows and columns.
                if val == ".": # checks if value is "."
                    continue # if it is go back to the second loop
                
                if val in rows[r]: # If val exists in rows, return false, the sudoku is not valid
                    return False
                if val in cols[c]: # same for cols, they work literally the same
                    return False
                if val in boxes.get((r//3, c//3), set()): # this creates in boxes a total of 9 sets, if needed, and is checking if val value... yeah... is in the current one
                    return False 
                # Rookie mistake... I forgot this part
                rows[r].add(val) # add the value to rows, otherwise it will always be true, yeah I forgot 
                cols[c].add(val) # add the value to cols
                if (r//3, c//3) not in boxes: # this all just to add the value to the set in the box, maybe there is a better way, my head hurt
                    boxes[(r//3, c//3)] = set()
                boxes[(r//3, c//3)].add(val)
        return True
# --- Test 
sol = Solution()
print(sol.isValidSudoku(board))

# I had to comment this code since I was losing my mind somehow, whatever, it works and I thinkg is good enough, I'm done wuith this