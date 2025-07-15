# https://leetcode.com/problems/check-if-any-element-has-prime-frequency/description/
# You are given an integer array nums.
# Return true if the frequency of any element of the array is prime, otherwise, return false.
# The frequency of an element x is the number of times it occurs in the array.
# A prime number is a natural number greater than 1 with only two factors, 1 and itself.

# Example 1:
# Input: nums = [1,2,3,4,5,4]
# Output: true
# Explanation:
# 4 has a frequency of two, which is a prime number.
nums = [1,2,3,4,5,4]
# --- My solution
class Solution:
    def checkPrimeFrequency(self, nums) -> bool:
        def isPrime(d):
            if d <= 1:
                return False
            if d == 2:
                return True
            if d % 2 == 0:
                return False
            for i in range(3, int(d**0.5) + 1, 2):
                if d % i == 0:
                    return False
            return True

        c = {}
        for n in nums:
            c[n] = c.get(n , 0) + 1

        for d in c.values():
            if isPrime(d):
                return True
        return False
        
# --- Test
sol = Solution()
print(sol.checkPrimeFrequency(nums))