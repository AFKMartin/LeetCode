# https://leetcode.com/problems/expression-add-operators/description
# Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.
# Note that operands in the returned expressions should not contain leading zeros.
# Note that a number can contain multiple digits.

# Example 1:

# Input: num = "123", target = 6
# Output: ["1*2*3","1+2+3"]
# Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
num = "123"
target = 6
# --- My solution
class Solution:
    def addOperators(self, num: str, target: int):
        res = []
        # backtrack function
        def bt(index, path, current, last):
            # base case: reached end of the string
            if index == len(num):
                if current == target:
                    res.append(path)
                
                return
            
            for i in range(index, len(num)):
                # skip numbers with leading zeros
                if i != index and num[index] == "0":
                    break

                part = num[index:i+ 1]
                n = int(part)

                if index == 0:
                    # first number, no operatorr in front
                    bt(i+1, part, n, n)
                

                else:
                    # for +
                    bt(i+1, path+"+"+part, current+n, n)

                    # for -
                    bt(i+1, path+"-"+part, current-n, -n)

                    # for *
                    bt(i+1, path+"*"+part, current - last + last*n, last*n)
        
        bt(0, "", 0, 0)
        return res
# --- Test
sol = Solution()
print(sol.addOperators(num, target))