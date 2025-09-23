# https://leetcode.com/problems/sum-of-two-integers/description
# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:

# Input: a = 1, b = 2
# Output: 3
a = 1
b = 2
# --- My solution
import math
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        

        while b != 0:
            c = (a & b) & MASK 
            a = (a ^ b) & MASK
            b = (c << 1) & MASK
        
        MAX = 0x7FFFFFFF
        return a if a <= MAX else ~(a ^ MASK)
        
# --- Test
sol = Solution()
print(sol.getSum(a, b))