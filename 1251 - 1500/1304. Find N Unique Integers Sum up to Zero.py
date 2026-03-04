# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/
# Given an integer n, return any array containing n unique integers such that they add up to 0.

# Example 1:

# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
n = 5
# --- My solution
class Solution:
    def sumZero(self, n):
        res = []
        c = n//2
        
        if n % 2 != 0:
            res.append(0)
        
        while c != 0:
            res.append(-c)
            res.append(c)
            c -= 1
        
        return res
# --- Test
sol = Solution()
print(sol.sumZero(n))