# https://leetcode.com/problems/generate-parentheses/description/
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# 
# Example 2:
# Input: n = 1
# Output: ["()"]
from typing import List
n = 3
# --- My solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        def backtrack(current, open, close):
            if len(current) == 2 * n:
                s.append(current)
                return
            if open < n:
                backtrack(current + "(", open + 1, close)
            if close < open:
                backtrack(current + ")", open, close + 1)
        backtrack("", 0, 0)
        return s
# --- Test
sol = Solution()
print(sol.generateParenthesis(n))