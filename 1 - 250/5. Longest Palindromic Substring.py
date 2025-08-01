# https://leetcode.com/problems/longest-palindromic-substring/description/
# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

s = "babad"
# --- My solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        x = "^#" + "#".join(s) + "#$"
        l = len(x)
        p = [0] * l
        c = r = 0
        for i in range(1, l - 1):
            mirror = 2*c - i
            if i < r:
                p[i] = min(r - i, p[mirror])
                return p[i]

            while x[i + 1 + p[i]] == x[i - 1 - p[i]]:
                p[i] += 1

            if i + p[i] > r:
                c, r = i, i + p[i]
        max_len = max(p)
        center = p.index(max_len)
        start = (center - max_len) // 2
        return s[start: start + max_len]
# --- Test 
sol = Solution()
print(sol.longestPalindrome(s))