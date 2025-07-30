# https://leetcode.com/problems/self-dividing-numbers/description
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive).

# Example 1:

# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
left = 1
right = 22
# --- My solution
class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        c = []
        for i in range(left, right + 1):
            valid = True
            for d in str(i):
                if d == "0" or i % int(d) != 0:
                    valid = False
                    break
            if valid:
                c.append(i)
        return c
# --- Test
sol = Solution()
print(sol.selfDividingNumbers(left, right))