# https://leetcode.com/problems/multiply-strings/description
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
num1 = "2"
num2 = "3"
# --- My solution
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        x, y = len(num1), len(num2)
        res = [0] * (x + y)

        for i in range(x -1, -1, -1):
            d1 = ord(num1[i]) - ord("0")
            for j in range(y -1, -1, -1):
                d2 = ord(num2[j]) - ord("0")
                product = d1*d2

                suma = product + res[i + j + 1]

                res[i + j + 1] = suma % 10
                res[i + j] += suma // 10
        
        c = 0
        while c < len(res) and res[c] == 0:
            c += 1
        
        return "".join(str(d) for d in res[c:])

# --- Test
sol = Solution()
print(sol.multiply(num1, num2))