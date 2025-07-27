# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description
# Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
# Note: You are not allowed to use any built-in library method to directly solve this problem.
 
# Example 1:

# Input: num = 26
# Output: "1a"
num = -1
# --- My solution
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_ch = "0123456789abcdef"
        res = []
        num &= 0xFFFFFFFF

        while num > 0:
            d = num & 0b1111
            res.append(hex_ch[d])
            num >>= 4
        return "".join(reversed(res))

# --- Test
sol = Solution()
print(sol.toHex(num))