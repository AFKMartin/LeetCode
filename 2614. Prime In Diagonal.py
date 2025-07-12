# https://leetcode.com/problems/prime-in-diagonal/description/
# You are given a 0-indexed two-dimensional integer array nums.
# Return the largest prime number that lies on at least one of the diagonals of nums. In case, no prime is present on any of # the diagonals, return 0.
# Note that:

# An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
# An integer val is on one of the diagonals of nums if there exists an integer i for which nums[i][i] = val or an i for which nums[i][nums.length - i - 1] = val.

# Example 1:

# Input: nums = [[1,2,3],[5,6,7],[9,10,11]]
# Output: 11
# Explanation: The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one of the diagonals. Since 11 is the largest prime, we return 11.
nums = [[1,2,2],[5,6,7],[9,10,10]]
# --- My solution
class Solution:
    def diagonalPrime(self, nums) -> int:
        def isPrime(n):
            if n <= 1:
                return False
            if n <= 3:
                return n > 1
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        n = len(nums)
        diag = set()

        for i in range(n):
            diag.add(nums[i][i]) # principal
            diag.add(nums[i][n - 1 - i]) # secondary
        
        diagonalPrimes = [x for x in diag if isPrime(x)]

        return max(diagonalPrimes) if diagonalPrimes else 0       

# --- Test
sol = Solution()
print(sol.diagonalPrime(nums))