# https://leetcode.com/problems/daily-temperatures/description/
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# --- My solution
class Solution:
    def dailyTemperatures(self, temperatures):
        s = []
        a = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while s and temperatures[i] > temperatures[s[-1]]:
                p = s.pop()
                a[p] = i-p
            s.append(i)
        return a     
# --- Test
temperatures = [73,74,75,71,69,72,76,73]
sol = Solution()
print(sol.dailyTemperatures(temperatures))