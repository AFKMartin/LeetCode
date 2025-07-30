# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

sentence = "qazwsxedcrfvtgbyhnujmikolp"
# --- My solution
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

# --- Test 
sol = Solution()
print(sol.checkIfPangram(sentence))

