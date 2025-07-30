# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
from typing import List
# --- My solution
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                stack.append((-1)*stack.pop() + stack.pop())
            elif t == "/":
                stack.append(int((1/stack.pop()) * stack.pop()))
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(t)) 
        return stack[0]
# --- Test
sol = Solution()
print(sol.evalRPN(tokens = ["4","13","5","/","+"]))

# This one is works, and did pass the test, but for some reason I didn't use (a b) logic, that might be better.
