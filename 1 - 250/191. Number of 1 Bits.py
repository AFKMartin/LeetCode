# https://leetcode.com/problems/number-of-1-bits/
# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.
n = 11
# --- My solution
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

# --- Test
sol = Solution() 
print(sol.hammingWeight(n))