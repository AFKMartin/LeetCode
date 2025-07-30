# https://leetcode.com/problems/top-k-frequent-elements/description/
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
from typing import List
nums = [1,1,1,2,2,3,3]
k = 2
# --- My solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        f = [[] for x in range(len(nums) + 1)]

        for n in nums:
            m[n] = m.get(n, 0) + 1

        for n, c in m.items():
            f[c].append(n)
        
        res = []
        for i in range(len(f) -1, 0, -1):
            for n in f[i]:
                res.append(n)
                if len(res) == k:
                    return res
# --- Test
sol = Solution()
print(sol.topKFrequent(nums, k))