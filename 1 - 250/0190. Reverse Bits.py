# https://leetcode.com/problems/reverse-bits/description/
# Reverse bits of a given 32 bits signed integer.

# Example 1:

# Input: n = 43261596
# Output: 964176192
# Explanation:
# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000
n = 43261596
# --- My solution
class Solution:
    def reverseBits(self, n: int) -> int:
        
        b32 = bin(n)[2:].zfill(32)
        reversedb = b32[::-1]

        return int(reversedb, 2)
        

# --- Test
sol = Solution()
print(sol.reverseBits(n))