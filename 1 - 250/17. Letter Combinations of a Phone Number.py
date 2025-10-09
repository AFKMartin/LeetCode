# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
digits = "23"
# --- My solution
class Solution:
    def letterCombinations(self, digits: str):
        if not digits: # edge case
            return []
        
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        } # map the phone with a dictionary

        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append("".join(path)) # append values back and forth
                return 
            
            for letter in phone_map[digits[index]]:
                backtrack(index + 1, path + [letter])

        backtrack(0, [])
        return res
# --- Test
sol = Solution()
print(sol.letterCombinations(digits))