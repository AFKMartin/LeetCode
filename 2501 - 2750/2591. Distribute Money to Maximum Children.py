# https://leetcode.com/problems/distribute-money-to-maximum-children/description
# You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.
# You have to distribute the money according to the following rules:
# All money must be distributed.
# Everyone must receive at least 1 dollar.
# Nobody receives 4 dollars.
# Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.

# Example 1:

# Input: money = 20, children = 3
# Output: 1
# Explanation: 
# The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money is:
# - 8 dollars to the first child.
# - 9 dollars to the second child. 
# - 3 dollars to the third child.
# It can be proven that no distribution exists such that number of children getting 8 dollars is greater than 1.
money = 16
children = 2
# --- My solution
class Solution:
    def distMoney(self, money, children):
        if money < children:
            return -1
        
        remain = money - children
        maximum8 = min(remain // 7, children)

        while maximum8 >= 0:
            lefts = remain - 7 * maximum8
            other = children - maximum8

            if lefts == 0:
                return maximum8
            if other > 0 and not (other == 1 and lefts == 3):
                return maximum8
            
            maximum8 -= 1
        
        return -1
# --- Test
sol = Solution()
print(sol.distMoney(money, children))