# https://leetcode.com/problems/valid-parentheses/description/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Example 1:
# Input: s = "()"
# Output: true
s = "(())"
# --- My solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        map = {')': '(', '}': '{', ']': '['} 
        for char in s: 
            if char in map: 
                top = stack.pop() if stack else "#" 
                if map[char] != top: 
                    return False 
            else:
                stack.append(char)
        return not stack 
# --- Test 
sol = Solution()
print(sol.isValid(s))