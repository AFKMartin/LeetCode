# https://leetcode.com/problems/three-divisors/description/
# Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.
# An integer m is a divisor of n if there exists an integer k such that n = k * m.

# Example 1:

# Input: n = 2
# Output: false
# Explantion: 2 has only two divisors: 1 and 2.
n = 25
# --- My solution
class Solution:
    def isThree(self, n: int) -> bool:
        root = 1
        while root * root < n:
            root += 1
        if root * root != n:
            return False
        if root < 2:
            return False
        for i in range(2, root):
            if root % i == 0:
                return False
        return True

# just check if the sqrt of the number is prime, if so, n will always have 3 divisors 
# --- Test
sol = Solution()
print(sol.isThree(n))