# https://leetcode.com/problems/basic-calculator/description
# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every num and running calculation will fit in a signed 32-bit integer.

# Example 1:

# Input: s = "1 + 1"
# Output: 2
s = "1 + 1"
# --- My solution
class Solution:
    def calculate(self, s: str) -> int:
        c = []
        res = 0
        num = 0
        sign = 1 # 1 for positive -1 for negative
        i = 0

        while i < len(s): # loop through s
            char = s[i]

            if char.isdigit():  # check if the character is a digit (0-9)
                num = 0
                while i < len(s) and s[i].isdigit():  # build the full number if it has multiple digits
                    num = num * 10 + int(s[i])  # shift previous digits left and add current digit
                    i += 1  # move to the next character
                res += sign * num  # add the number to the result with its sign (+/-)
                continue  # skip the i increment at the end of the main loop since we already moved i

            elif char == "+":
                sign = 1 # checks if the symbol is positive (+), if so, sign is 1
            
            elif char == "-":
                sign = -1 # checks if the symbol is negative (-), if so, sign is -1
            
            elif char == "(":
                # checks if the symbol is open parenthesis ("("), if so, push current res and sign onto stack
                c.append(res)
                c.append(sign)
                res = 0
                sign = 1
            
            elif char == ")":
                # checks if the symbol is closing parenthesis (")"), if so, pop previous res and sign out of the stack
                prevSign = c.pop()
                prevRes = c.pop()
                res = prevRes + prevSign * res
            
            # skip spaces
            i += 1

        return res

# --- test
sol = Solution()
print(sol.calculate(s))
