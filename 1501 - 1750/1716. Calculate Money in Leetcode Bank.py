# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description
# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

# Example 1:

# Input: n = 4
# Output: 10
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
n = 20
# --- My solution
class Solution:
    def totalMoney(self, n):
        x, y, res = 0, 1, 0
        
        while x < n:
            res += y
            y += 1
            x += 1
 
            if x % 7 == 0:
                y = 1 + x // 7
        
        return res
# --- Test
sol = Solution()
print(sol.totalMoney(n))