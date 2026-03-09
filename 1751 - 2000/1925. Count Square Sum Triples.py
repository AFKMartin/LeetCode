# https://leetcode.com/problems/count-square-sum-triples/description
# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
# Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

# Example 1:

# Input: n = 5
# Output: 2
# Explanation: The square triples are (3,4,5) and (4,3,5).
n = 10
# --- My solution
class Solution:
    def countTriples(self, n):
        squares = set(i * i for i in range(1, n + 1))
        res = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a * a + b * b in squares and (a * a + b * b) ** 0.5 <= n:
                    res += 1
        return res        
# --- Test
sol = Solution()
print(sol.countTriples(n))
