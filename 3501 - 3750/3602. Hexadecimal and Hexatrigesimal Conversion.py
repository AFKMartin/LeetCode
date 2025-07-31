# https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/description
# You are given an integer n.
# Return the concatenation of the hexadecimal representation of n2 and the hexatrigesimal representation of n3.
# A hexadecimal number is defined as a base-16 numeral system that uses the digits 0 – 9 and the uppercase letters A - F to represent values from 0 to 15.
# A hexatrigesimal number is defined as a base-36 numeral system that uses the digits 0 – 9 and the uppercase letters A - Z to represent values from 0 to 35.

# Example 1:
# Input: n = 13
# Output: "A91P1"
# Explanation:
# n2 = 13 * 13 = 169. In hexadecimal, it converts to (10 * 16) + 9 = 169, which corresponds to "A9".
# n3 = 13 * 13 * 13 = 2197. In hexatrigesimal, it converts to (1 * 362) + (25 * 36) + 1 = 2197, which corresponds to "1P1".
# Concatenating both results gives "A9" + "1P1" = "A91P1".
n = 13
# --- My solution
class Solution:
    def concatHex36(self, n: int) -> str:
        p2 = n ** 2
        p3 = n ** 3
        def tobase36(p3):
            ch = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            res = ""
            while p3 > 0:
                p3, r = divmod(p3, 36)
                res = ch[r] + res
            return res or "0"
        def tobase16(p2):
            ch = "0123456789ABCDEF"
            res = ""
            while p2 > 0:
                p2, r = divmod(p2, 16)
                res = ch[r] + res
            return res or "0"
        x = tobase36(p3)
        y = tobase16(p2)
        return str(y + x)  
# --- Test
sol = Solution()
print(sol.concatHex36(n))