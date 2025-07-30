# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
s = "abcabcbb"
# --- My solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        for w in range(n):
            l = set()
            for i in range(w, n):
                if s[i] in l:
                    break
                l.add(s[i])
            res = max(res, len(l))
        return res
# This code is pretty slow, dunno how to do it better, but it works so...
# --- Test
sol = Solution()
print(sol.lengthOfLongestSubstring(s))