# https://leetcode.com/problems/valid-palindrome-ii/description/
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:

# Input: s = "aba"
# Output: true
s = "aba"
# --- My solution
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(sub):
            return sub == sub[::-1]
        
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                skip_left = s[left+1:right+1]
                skip_right = s[left:right]
                return isPalindrome(skip_left) or isPalindrome(skip_right)
            left +=1
            right -=1
        return True
# --- Test
sol = Solution()
print(sol.validPalindrome(s))