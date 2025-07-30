# https://leetcode.com/problems/count-primes/description/
# Given an integer n, return the number of prime numbers that are strictly less than n.
# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
n = 100
# --- My solution
# without numpy is super slow, this gave me 1265ms and pass the test, the last version was too slow to do so
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        return sum(is_prime)
        
# --- Test
sol = Solution()
print(sol.countPrimes(n))