# https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=prshgx6i
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.
s = "aaaaaaaaaabbbccddd"
# --- My solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for l in s:
            counter[l] = counter.get(l, 0) + 1
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1

# --- Test 
sol = Solution()
print(sol.firstUniqChar(s))