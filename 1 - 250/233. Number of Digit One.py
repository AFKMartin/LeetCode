# https://leetcode.com/problems/number-of-digit-one/description
# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
# Example 1:

# Input: n = 13
# Output: 6
n = 13
# --- My solution
class Solution:
    def countDigitOne(self, n: int) -> int:
        c = 0
        p = 1
        # loop through each digit position (1, 10, 100 ...)
        while p <= n:
            left = n // (p * 10) # digits to the left, example: n = 13 // (1*10) = 1
            current = (n // p) % 10 # current, example: n = 13 // 1 = 13 % 10 = 3
            right = n % p # digis to the right, example: 13 % 1 = 0
            # if current is 0, means only full cycles from left matters
            if current == 0:
                c += left * p
            # if current is 1, means full cycles from left + numbers formed by right + 1   
            elif current == 1:
                c += left * p + right + 1
            # any other value, means full cycles from left + 1 extra cycle    
            else:
                c += (left + 1) * p
            # moves to the next higher digit position (p = 1, p = 10, p = 100...)
            p *= 10

        return c
# --- Test
sol = Solution()
print(sol.countDigitOne(n))