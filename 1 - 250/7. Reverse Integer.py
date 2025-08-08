# https://leetcode.com/problems/reverse-integer/description/
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
x = 123
# --- My solution
class Solution:
    def reverse(self, x: int) -> int:
        s = -1 if x < 0 else 1
        x_abs = abs(x)
        
        rever_str = str(x_abs)[::-1]
        rever_int = int(rever_str)

        res = s * rever_int

        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res

# --- Test 
sol = Solution()
print(sol.reverse(x))