# https://leetcode.com/problems/divide-two-integers/description
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
dividend = 7
divisor = -3
# --- My solution
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # In case of overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        x, y = abs(dividend), abs(divisor)
        res = 0

        while x >= y:
            temp, c = y, 1
            while x >= (temp + temp):
                temp += temp
                c += c
            x -= temp
            res += c

        # Checks the sign
        if (dividend < 0) ^ (divisor < 0):
            res = -res

        return res

# --- Test
sol = Solution()
print(sol.divide(dividend, divisor)) 
