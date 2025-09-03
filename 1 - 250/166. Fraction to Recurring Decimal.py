# https://leetcode.com/problems/fraction-to-recurring-decimal/description
# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# If multiple answers are possible, return any of them.
# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"
numerator = 1
denominator = 2
# --- My solution
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # if numerator is 0, the result will always be 0, no matter the value of denominator
        if numerator == 0:
            return "0"
        
        res = []     
        # If one of the numbers, numerator or denominator is 0, we know the result is negative
        if (0 > numerator) ^ (0 > denominator):
            res.append("-")
        # conver the values to abs so we don't handle signs anymore since we alredy did
        numerator, denominator = abs(numerator), abs(denominator)
        # append the value of the division as a str
        res.append(str(numerator // denominator))
        # save the value of the remainder to handle it later
        remainder = numerator % denominator
        # if the remainder is 0 just return the res value at this point
        if remainder == 0:
            return "".join(res)
        # Otherwise, there is a fractional part so add a dot to it
        res.append(".")
        # log division manually
        s = {}
        while remainder:
            # if the remainder has been seen before we know there is cycle
            if remainder in s:
                # position of in res where this remainder first appeared
                x = s[remainder]
                # insert "(" at that position
                res.insert(x, "(")
                # close the cycle ")"
                res.append(")")
                break
            # store the position of this remainder in the result
            s[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        # join list into a string and return
        return "".join(res)
# --- Test
sol = Solution()
print(sol.fractionToDecimal(numerator, denominator))