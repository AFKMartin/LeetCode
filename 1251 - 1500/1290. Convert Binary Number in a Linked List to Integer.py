# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
# The most significant bit is at the head of the linked list.

# Example 1:

# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
head = [1,0,1]
# --- My solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
        bits = [] 
        while head:
            bits.append(str(head.val))  # store as string directly
            head = head.next
        return int("".join(bits), 2) # convert to decimal       
# --- Test
sol = Solution()
print(sol.getDecimalValue(head))