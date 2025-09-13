# https://leetcode.com/problems/perfect-squares/description
# Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
n = 12
# --- My solution
class Solution:
    def numSquares(self, n: int) -> int:
        # generate all perfect squares <= n
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        
        # min number of squares summing to i
        dp = [float("inf")] * (n + 1)
        dp[0] = 0  # 0 requires 0 squares
         
        # for each i, dp[i] is the minimum number of perfect squares needed, computed from smaller sums by adding one square at a time
        for i in range(1, n + 1):
            for sq in squares:
                if sq <= i:
                    dp[i] = min(dp[i], dp[i - sq] + 1)
        
        return dp[n]
    # If you go greedy version like sqrt of 12 = 3.46... and start trying every combination from 1, 4, 9 it might take a lot of time but you can do it too, might be better for smaller numbers.
# --- Test
sol = Solution()
print(sol.numSquares(n))


'''
This solution is not mine but is way better

class Solution:
    def numSquares(self, n: int) -> int:
        def is_square(x): 
            r = isqrt(x); return r*r == x

        if is_square(n): 
            return 1

        # remove 4^a factor
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4

        # check sum of two squares
        r = isqrt(n)
        for a in range(1, r + 1):
            if is_square(n - a*a):
                return 2
        return 3

Since it uses Lagrange’s Four-Square Theorem:

"Every natural number can be written as the sum of at most four perfect squares."

Wich is brilliant.
'''