# https://leetcode.com/problems/basic-calculator-ii/description
# Given a string s which represents an expression, evaluate this expression and return its value. 
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.

# Example 1:

# Input: s = "3+2*2"
# Output: 7

s = s = "3+2*2"
# --- My solution
class Solution:
    def calculate(self, s: str) -> int:
        c = []
        num = 0
        sign = "+"

        for i, char in enumerate(s):
            if char.isdigit(): # checks if char is a digit (0-9)
                num = num * 10 + int(char) # if so, num is num * 10 + char (converted to an int)
            
            if char in "+-*/" or i == len(s) - 1:  # process the previous number when an operator or end is reached
                if sign == "+":  # previous operator was +, append num
                    c.append(num)

                elif sign == "-":  # previous operator was -, append -num
                    c.append(-num)

                elif sign == "*":  # previous operator was *, pop last number, multiply by num, and push back
                    c.append(c.pop() * num)

                elif sign == "/":  # previous operator was /, pop last number, divide by num (truncate toward zero), push back
                    x = c.pop()
                    c.append(int(x / num))

                sign = char
                num = 0
        return sum(c) # return the sum of c

# --- Test
sol = Solution()
print(sol.calculate(s))