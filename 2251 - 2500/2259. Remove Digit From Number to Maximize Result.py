# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/
# You are given a string number representing a positive integer and a character digit.

# Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.

# Example 1:

# Input: number = "123", digit = "3"
# Output: "12"
# Explanation: There is only one '3' in "123". After removing '3', the result is "12".
number = "1231"
digit = "1"
# --- My Solution
class Solution:
    def removeDigit(self, number, digit):
        res = [
            number[:i] + number[i+1:]
            for i in range(len(number))
            if number[i] == digit
        ]
        return max(res)

# --- Test 
sol = Solution()
print(sol.removeDigit(number, digit))