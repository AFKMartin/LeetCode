# https://leetcode.com/problems/longest-common-prefix/description/
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
strs = ["flower","flow","flight"]
# --- My solution
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        
        size = min(len(word) for word in strs)
        wsize = len(strs)

        for i in range(size):
            char = strs[0][i]

            for j in range(1, wsize):
                if strs[j][i] != char:
                    return strs[0][:i]
        
        return strs[0][:size]
    
# I hate double loops

# --- Test
sol = Solution()
print(sol.longestCommonPrefix(strs))