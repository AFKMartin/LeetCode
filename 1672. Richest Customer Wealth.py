# https://leetcode.com/problems/richest-customer-wealth/description/
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

# Example 1:

# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.
accounts = [[1,2,3],[3,2,1]]
# --- My solution
class Solution:
    def maximumWealth(self, accounts) -> int:
        return max(sum(a) for a in accounts)

# --- Test 
sol = Solution()
print(sol.maximumWealth(accounts))