# https://leetcode.com/problems/factorial-trailing-zeroes/description
# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
# Example 1:
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
n = 5
# --- My solution
class Solution:
    def trailingZeroes(self, n: int) -> int:
        c = 0
        # count how many factors of 5 are in n!
        # each factor of 5 paired with a factor of 2 gives a trailing zero
        while n >= 5: 
            n //= 5 # count multiples of 5: 25, 125, and so on...
            c += n # add them to total trailing zeros
        return c

# --- Test
sol = Solution()
print(sol.trailingZeroes(n))

'''
Trailing zeros = count of factors of 5 in n!
- 5! = 120                                 5//5 = 1 -> 1 zero 
- 10! = 3,628,800                          10//5 = 2 -> 2 zeros
- 15! = 1,307,674,368,000                  15//5 = 3 -> 3 zeros
- 20! = 2,432,902,008,176,640,000          20//5 = 4 -> 4 zeros
'''