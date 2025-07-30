# https://leetcode.com/problems/find-words-containing-character/description/
# You are given a 0-indexed array of strings words and a character x.
# Return an array of indices representing the words that contain the character x.
# Note that the returned array may be in any order.

# Example 1:

# Input: words = ["leet","code"], x = "e"
# Output: [0,1]
# Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
words = ["leet","code"]
x = "e"
# --- My solution
class Solution:
    def findWordsContaining(self, words, x: str):
        return [i for i, word in enumerate(words) if x in word]
# --- Test
sol = Solution()
print(sol.findWordsContaining(words, x))


