# https://leetcode.com/problems/count-integers-with-even-digit-sum/description
# Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.
# The digit sum of a positive integer is the sum of all its digits.

# Example 1:

# Input: num = 4
# Output: 2
# Explanation:
# The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    
num = 30
# --- My solution
class Solution:
    def countEven(self, num):
        c = sum(int(d) for d in str(num))
        if c % 2 == 0:
            return num // 2
        else:
            return (num - 1) // 2

# --- Test
sol = Solution()
print(sol.countEven(num))