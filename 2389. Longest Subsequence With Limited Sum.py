# https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/
# You are given an integer array nums of length n, and an integer array queries of length m.
# Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

# Example 1:

# Input: nums = [4,5,2,1], queries = [3,10,21]
# Output: [2,3,4]
# Explanation: We answer the queries as follows:
# - The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
# - The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
# - The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
nums = [4,5,2,1]
queries = [3,10,21]
# --- My Solution
class Solution:
    def answerQueries(self, nums, queries):
        snums = sorted(nums)
        prefix = []
        total = 0
        for n in snums: 
            total += n 
            prefix.append(total) 
        ans = [] 
        for q in queries: 
            c = 0 
            for s in prefix: 
                if s <= q: # if the acc sum is less or equl to q
                    c += 1 # add 1 to c
                else:
                    break # else, break
            ans.append(c) # when breaking, appnend the value of c to the answer
        return ans
# Looping might not be the best way, but could't find another one, dunno.
# 75 ms Beats 28.01%
# --- Test
sol = Solution()
print(sol.answerQueries(nums, queries))