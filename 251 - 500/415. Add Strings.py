# https://leetcode.com/problems/add-strings/description
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
num1 = "11"
num2 = "123"
# --- My solution
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        c = 0
        res = []

        while i >= 0 or j >= 0 or c:
            d1 = int(num1[i]) if i >= 0 else 0
            d2 = int(num2[j]) if j >= 0 else 0

            total = d1 + d2 + c
            c = total // 10
            res.append(str(total % 10))

            i -= 1
            j -= 1
        
        return "".join(res[::-1])
    
# This is more complicated than it should be because one of the test has more than 4300 digits for whatever reason
# --- Test
sol = Solution()
print(sol.addStrings(num1, num2))