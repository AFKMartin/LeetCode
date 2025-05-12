# https://leetcode.com/problems/group-anagrams/
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
from typing import List
strs = ["eat","tea","tan","ate","nat","bat"]
# --- My solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for w in strs:
            k = ''.join(sorted(w))
            if k in m:
                m[k].append(w)
            else:
                m[k] = [w]
        return list(m.values())
# --- Test 
sol = Solution()
print(sol.groupAnagrams(strs))