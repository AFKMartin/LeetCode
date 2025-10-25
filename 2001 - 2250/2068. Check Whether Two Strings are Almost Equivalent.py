# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/description/
# Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.
# Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.
# The frequency of a letter x is the number of times it occurs in the string.

# Example 1:

# Input: word1 = "aaaa", word2 = "bccb"
# Output: false
# Explanation: There are 4 'a's in "aaaa" but 0 'a's in "bccb".
# The difference is 4, which is more than the allowed 3
word1 = "aaaa"
word2 = "bccb"
# --- My solution
from collections import Counter
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        for c in set(c1.keys()) | set(c2.keys()):
            if abs(c1.get(c, 0) - c2.get(c, 0)) > 3:
                return False
        return True

# --- Test
sol = Solution()
print(sol.checkAlmostEquivalent(word1, word2))