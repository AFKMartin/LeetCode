# https://leetcode.com/problems/different-ways-to-add-parentheses/description
# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.
# The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

# Example 1:

# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
expression = "2-1-1"
# --- My solution
class Solution:
    def diffWaysToCompute(self, expression: str):
        m = {}
        
        # if we've already computed results for this substring, return cached version
        def ways(exp):
            if exp in m:
                return m[exp]
            
            res = []
            if exp.isdigit(): # if exp is a whole number, convert to int and return it
                res.append(int(exp))
            else:
                for i, char in enumerate(exp):
                    if char in "+-*/": # if the character is an operator, use it as a split point
                        left = ways(exp[:i]) # everything BEFORE the operator
                        right = ways(exp[i+1:]) # everything AFTER the operator
                        
                        for l in left: # combine every left result with every right result using the operator
                            for r in right:
                                if char == "+":
                                    res.append(l + r)
                                
                                elif char == "-":
                                    res.append(l - r)

                                elif char == "*":
                                    res.append(l * r)
                                
                                # elif char == "/":
                                #     res.append(l // r) # just realized this is not needed
            m[exp] = res
            return res
        
        return ways(expression)
                
# --- Test
sol = Solution()
print(sol.diffWaysToCompute(expression))