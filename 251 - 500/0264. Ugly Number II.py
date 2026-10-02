# https://leetcode.com/problems/ugly-number-ii/description
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return the nth ugly number.

# Example 1:

# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
n = 10
# --- My solution
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n  # ugly[i] will store the (i+1)-th ugly number
        i2 = i3 = i5 = 0  
        
        for k in range(1, n):
            # Generate the next possible ugly numbers from current pointers
            next2, next3, next5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5  
            
            # The next ugly number is the smallest among these candidates
            ugly[k] = min(next2, next3, next5)
            
            # Move forward any pointer(s) that match the chosen value, this way we avoid duplicates like 6 = 2 * 3 = 3 * 2
            if ugly[k] == next2:
                i2 += 1 
            if ugly[k] == next3:
                i3 += 1
            if ugly[k] == next5:
                i5 += 1
        
        return ugly[-1]  # The nth ugly number is the last in the array
# --- Test
sol = Solution()
print(sol.nthUglyNumber(n))