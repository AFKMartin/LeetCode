# https://leetcode.com/problems/super-ugly-number/description
# A super ugly number is a positive integer whose prime factors are in the array primes.
# Given an integer n and an array of integers primes, return the nth super ugly number.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

# Example 1:

# Input: n = 12, primes = [2,7,13,19]
# Output: 32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].
n = 12
primes = [2,7,13,19]
# --- My solution
class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        res = [1] * n # sequence of ugly numbers
        k = len(primes) # number of primes
        index = [0] * k # pointers for each prime
        val = primes[:] # candidate values for each prime

        for i in range(1, n):
            minimum = min(val) # smallest candidate
            res[i] = minimum # next ugly number

            for j in range(k):
                if val[j] == minimum: # update all primes that matched min
                    index[j] += 1
                    val[j] = primes[j] * res[index[j]]

        return res[-1] # return the last value of res since is what they ask us to do

# --- Test
sol = Solution()
print(sol.nthSuperUglyNumber(n, primes))