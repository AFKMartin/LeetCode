# https://leetcode.com/problems/super-pow/description
# Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

# Example 1:

# Input: a = 2, b = [3]
# Output: 8
a = 2
b = [4,3,3,8,5,2]
# --- My solution
class Solution:
    def superPow(self, a: int, b) -> int:
        c = 1
        for d in b:
            c = pow(c, 10, 1337) * pow(a, d, 1337) % 1337
            # Update c: shift exponent left by one decimal place (c^10) then add the new digit d (multiplied by a^d), all under modulo 1337 as the problem dictates
            # If doing return (a ** b)%1337 (b converted to an int) it might fail because b in the test can be super high
        return c
        
# --- Test
sol = Solution()
print(sol.superPow(a, b))