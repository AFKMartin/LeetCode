# https://leetcode.com/problems/regular-expression-matching/description/
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
s = "aa"
p = "a"

# --- My solution
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        c = {}

        def dp(i, j):
            if (i, j) in c:
                return c[(i, j)]
            
            if j == len(p):
                return i == len(s)
            
            first = i < len(s) and p[j] in {s[i], '.'}

            if j + 1 < len(p) and p[j + 1] == "*":
                ans = dp(i, j + 2) or (first and dp(i + 1, j))
            
            else:
                ans = first and dp(i + 1, j + 1)
            
            c[(i, j)] = ans
            return ans
        
        return dp(0,0)


# --- Test
sol = Solution()
print(sol.isMatch(s,p))