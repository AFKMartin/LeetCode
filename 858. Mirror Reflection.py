# https://leetcode.com/problems/mirror-reflection/description/
# There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.
# The square room has walls of length p and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.
# Given the two integers p and q, return the number of the receptor that the ray meets first.
# The test cases are guaranteed so that the ray will meet a receptor eventually.

# Example 1:

# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
p = 6
q = 4
# --- My solution
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)
        
        l = lcm(p, q)
        m = l // p
        n = l // q

        if m % 2 == 1 and n % 2 == 1:
            return 1
        elif m % 2 == 0 and n % 2 == 1:
            return 0
        else:
            return 2
    
''' 
The LCM, in our case, gives the least common "height" or distance where the laser returns to a corner.
Let m = LCM(p, q) // p -> number of vertical extensions (reflections on horizontal walls)
Let n = LCM(p, q) // q -> number of horizontal extensions (reflections on vertical walls)

- If m is odd and n is odd then the ray hits receptor 1 
- If m is even and n is odd then the ray hits receptor 0 
- If n is even → the ray hits receptor 2 (top-left corner), regardless of m...

Makes sense, try drawing it, it actually makes sense but is hard to explain with words.
'''
        
# --- Test
sol = Solution()
print(sol.mirrorReflection(p,q))