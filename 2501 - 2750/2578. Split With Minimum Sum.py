# https://leetcode.com/problems/split-with-minimum-sum/description
# Given a positive integer num, split it into two non-negative integers num1 and num2 such that:
# The concatenation of num1 and num2 is a permutation of num.
# In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.
# num1 and num2 can contain leading zeros.
# Return the minimum possible sum of num1 and num2.

# Notes:

# It is guaranteed that num does not contain any leading zeros.
# The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.
 
# Example 1:

# Input: num = 4325
# Output: 59
# Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59. We can prove that 59 is indeed the minimal possible sum.
num = 687
# --- My solution
class Solution:
    def splitNum(self, num):
        digits = sorted(str(num))
        num1 = ""
        num2 = ""
        for i, d in enumerate(digits):
            if i % 2 == 0:
                num1 += d
            else:
                num2 += d
        return int(num1) + int(num2)
# --- Test
sol = Solution()
print(sol.splitNum(num))