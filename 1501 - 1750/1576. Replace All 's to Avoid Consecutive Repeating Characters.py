# https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/description/
# Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.
# It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.
# Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

# Example 1:

# Input: s = "?zs"
# Output: "azs"
# Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
s = "?zs"
# --- My solution
class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == "?":
                for x in "abc": # only need 3 letters to ensure a valid result
                    if (i > 0 and s[i - 1] == x) or (i < len(s) - 1 and s[i + 1] == x): # Check the previous and next characters
                        continue # whatever, skip this letter and try the next one
                    s[i] = x

                    break
        return "".join(s)
# --- Test
sol = Solution()
print(sol.modifyString(s))