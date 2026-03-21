# https://leetcode.com/problems/k-items-with-the-maximum-sum/description
# There is a bag that consists of items, each item has a number 1, 0, or -1 written on it.
# You are given four non-negative integers numOnes, numZeros, numNegOnes, and k.
# The bag initially contains:
# numOnes items with 1s written on them.
# numZeroes items with 0s written on them.
# numNegOnes items with -1s written on them.
# We want to pick exactly k items among the available items. Return the maximum possible sum of numbers written on the items.

# Example 1:

# Input: numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2
# Output: 2
# Explanation: We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. We take 2 items with 1 written on them and get a sum in a total of 2.
# It can be proven that 2 is the maximum possible sum.
numOnes = 3
numZeros = 2
numNegOnes = 0
k = 4
# --- My solution
class Solution:
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        if k <= numOnes:
            return k
        
        k -= numOnes
        if k <= numZeros:
            return numOnes
        
        k -= numZeros
        if k <= numNegOnes:
            return numOnes - k
        
        return numOnes - numNegOnes 
# --- Test
sol = Solution()
print(sol.kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))
