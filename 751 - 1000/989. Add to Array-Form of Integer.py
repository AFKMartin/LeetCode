# https://leetcode.com/problems/add-to-array-form-of-integer/description
# The array-form of an integer num is an array representing its digits in left to right order.
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

# Example 1:

# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
num = [1,2,0,0]
k = 34
# --- My solution
class Solution:
    def addToArrayForm(self, num, k: int):
        res = []
        i = len(num) - 1

        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
                i -= 1
            res.append(k % 10)
            k //= 10

        return res[::-1]
# --- Test
sol = Solution()
print(sol.addToArrayForm(num, k))