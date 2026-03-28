# https://leetcode.com/problems/count-symmetric-integers/description
# You are given two positive integers low and high.
# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.
# Return the number of symmetric integers in the range [low, high].

# Example 1:

# Input: low = 1, high = 100
# Output: 9
# Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.
low = 1200
high = 1230
# --- My solution
class Solution:
    def countSymmetricIntegers(self, low, high):
        c = 0
        for i in range(low, high + 1):
            s = str(i)
            if len(s) % 2 == 0:
                n = len(s) // 2
                if sum(map(int, s[:n])) == sum(map(int, s[n:])):
                    c += 1
        return c      
# --- Test
sol = Solution()
print(sol.countSymmetricIntegers(low, high))