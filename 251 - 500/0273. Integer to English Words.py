# https://leetcode.com/problems/integer-to-english-words/description
# Convert a non-negative integer num to its English words representation.

# Example 1:

# Input: num = 123
# Output: "One Hundred Twenty Three"
num = 1234567
# --- My solution
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        # map below 20
        b20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
                    "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen",
                    "Eighteen","Nineteen"]
        
        # map of tens
        tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        
        # map of thousands
        thou = ["","Thousand","Million","Billion"]

        # def for bellow 1000
        def b1000(n):
            # if n == 0 just return "Zero"
            if n == 0: 
                return ""
            # if below 20 just use the b20 to return the string
            elif n < 20:
                return b20[n] + " "
            # for n < 100, for example 95, return: tens [95 // 10] = 9 = "Ninety" + (n % 10 = 5) wich uses the n < 20 case and returns "Five" adding both is "Ninety Five"
            elif n < 100:
                return tens[n // 10] + " " + b1000(n % 10)
            # Anything above 99 will use this case, for example 100: b20[n // 100] = b20[1] = "One" + " Hundred " + (n % 100) = "" wich leads to "One Hundred"
            else: 
                return b20[n // 100] + " Hundred " + b1000(n %100)
        
        res = ""            # final result string
        i = 0               # index for 'thou' scale: "", "Thousand", "Million", "Billion"
        while num > 0:      
            if num % 1000 != 0:  
                # convert last 3 digits to words and add the appropriate scale
                res = b1000(num % 1000) + thou[i] + " " + res
            num //= 1000    # remove last 3 digits and move to the next chunk
            i += 1          # move to next scale
        return res.strip()  # remove trailing spaces and return final result
    
# --- Test
sol = Solution()
print(sol.numberToWords(num))