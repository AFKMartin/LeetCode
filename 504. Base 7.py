# https://leetcode.com/problems/base-7/description
# Given an integer num, return a string of its base 7 representation.

# Example 1:

# Input: num = 100
# Output: "202"
num = -7
# --- My solution
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        neg = num < 0
        num = abs(num)

        c = []
        while num > 0:
            c.append(str(num % 7))
            num //= 7
        
        if neg:
            return "-" + "".join(reversed(c))
        else:
            return "".join(reversed(c))
sol = Solution()
print(sol.convertToBase7(num))