# https://leetcode.com/problems/greatest-common-divisor-of-strings/description
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
str1 = "ABCABC"
str2 = "ABC"

# --- My solution
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        # no common div
        if str1 + str2 != str2 + str1:
            return ""
        
        lngt = gcd(len(str1), len(str2))
        
        return str1[:lngt]

# --- Test
sol = Solution()
print(sol.gcdOfStrings(str1, str2))