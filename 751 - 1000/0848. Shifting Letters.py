# https://leetcode.com/problems/shifting-letters/description/
# You are given a string s of lowercase English letters and an integer array shifts of the same length.
# Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
# Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.
# Return the final string after all such shifts to s are applied.

# Example 1:

# Input: s = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation: We start with "abc".
# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.
s = "aaa"
shifts = [1,2,3]
# output = gfd
# --- My solution
class Solution:
    def shiftingLetters(self, s, shifts):
        def shift(c, x):
            return chr((ord(c) - ord('a') + x) % 26 + ord('a'))
        
        res = []
        
        suffix = 0
        sums = [0] * len(shifts)
        for i in range(len(shifts) - 1, -1, -1):
            suffix += shifts[i]
            sums[i] = suffix
           
        for i in range(len(s)):
            res.append(shift(s[i], sums[i]))
                
        return "".join(res)
      
# --- Test
sol = Solution()
print(sol.shiftingLetters(s, shifts))