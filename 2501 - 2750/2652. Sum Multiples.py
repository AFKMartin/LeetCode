# https://leetcode.com/problems/sum-multiples/description/
# Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.
# Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

# Example 1:

# Input: n = 7
# Output: 21
# Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.
n = 100
# --- My solution
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def sumDiv (k):
            m = n // k # 
            return k * m * (m + 1) // 2
        return sumDiv(3) + sumDiv(5) + sumDiv(7) - sumDiv(15) - sumDiv(21) - sumDiv(35) + sumDiv(105)
# --- Test 
sol = Solution()
print(sol.sumOfMultiples(n))

