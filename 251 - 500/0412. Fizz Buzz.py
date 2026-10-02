# https://leetcode.com/problems/fizz-buzz/description
# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]
n = 3
# --- My solution
class Solution:
    def fizzBuzz(self, n:int):
        lst = list(range(1, n + 1))
        c = ""
        res = []
        for l in lst:
            if l % 3 == 0 and l % 5 == 0:
                c = "FizzBuzz"
            elif l % 3 == 0:
                c = "Fizz"
            elif l % 5 == 0:
                c = "Buzz"
            else:
                c = str(l)
            res.append(c)
        return res
# --- Test
sol = Solution()
print(sol.fizzBuzz(n))