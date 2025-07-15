# https://leetcode.com/problems/count-primes/description/
# Given an integer n, return the number of prime numbers that are strictly less than n.
# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
n = 100
# --- My solution
class Solution:
    def countPrimes(self, n: int) -> int:
        def isPrime(num):
            if num <= 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for j in range(3, int(num**0.5) + 1, 2):
                if num % j == 0:
                    return False
            return True
        
        c = 0
        for i in range(2, n):
            if isPrime(i):
                c += 1
        return c
        
# --- Test
sol = Solution()
print(sol.countPrimes(n))