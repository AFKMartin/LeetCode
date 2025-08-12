# https://leetcode.com/problems/string-to-integer-atoi/description/
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
# The algorithm for myAtoi(string s) is as follows:
# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

# Example 1:
# Input: s = "42"
# Output: 42
# Explanation:

# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
# Step 2: "42" (no characters read because there is neither a '-' nor '+')       
# Step 3: "42" ("42" is read in)
s = "42"
# --- My solution
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        x = 1
        y = 0
        if s[0] == "-":
            x = -1
            y += 1
        elif s[0] == "+":
            y += 1
        
        n = 0
        while y < len(s) and s[y].isdigit():
            n = n * 10 + int(s[y])
            y += 1
        
        n *= x

        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        if n < MIN_INT:
            return MIN_INT
        if n > MAX_INT:
            return MAX_INT
        
        return n

# --- Test
sol = Solution()
print(sol.myAtoi(s))