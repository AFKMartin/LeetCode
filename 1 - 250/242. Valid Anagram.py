# https://leetcode.com/problems/valid-anagram/ 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Input: s = "anagram", t = "nagaram"
# Output: true
# Input: s = "rat", t = "car"
# Output: false
s = "nagaram"
t = "anagram"
# --- My Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for sc, tc in zip(s,t):
            countS[sc] = countS.get(sc, 0) + 1
            countT[tc] = countT.get(tc, 0) + 1
        return countS == countT 
# --- Test 
sol = Solution()
print(sol.isAnagram(s, t))
