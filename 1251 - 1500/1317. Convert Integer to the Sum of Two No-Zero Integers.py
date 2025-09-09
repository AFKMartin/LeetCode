# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description
# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.
# Given an integer n, return a list of two integers [a, b] where:
# a and b are No-Zero integers.
# a + b = n
# The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

# Example 1:

# Input: n = 2
# Output: [1,1]
# Explanation: Let a = 1 and b = 1.
# Both a and b are no-zero integers, and a + b = 2 = n.
n = 1
# --- My solution
class Solution:
    def getNoZeroIntegers(self, n: int):
        def noZero(x):
            return "0" not in str(x) # checks that x's decimal representation does NOT contain the digit "0"
        
        for a in range(1, n):
            b = n - a # basic formula of the problem
            if noZero(a) and noZero(b): # check that both, b and has no zeros
                return [a, b] # return the values
        

# --- Test
sol = Solution()
print(sol.getNoZeroIntegers(n))