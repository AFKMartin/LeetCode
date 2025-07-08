# https://leetcode.com/problems/add-two-numbers/description/
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
l1 = [2,4,3]
l2 = [5,6,4]
# ListNode Class
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# From python list to linked list
def ToLinkedList(lst):
    d = ListNode()
    current = d
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return d.next

# A way to print the Linked list to check output
def PrintLinkedList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# --- My solution
class Solution:
    def addTwoNumbers(self, l1, l2):
        res = ListNode()
        current = res
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return res.next

# I'm still bad as this time of problems took me more than I want to admit
# How is this med dif
# --- Test
sol = Solution()
print(sol.addTwoNumbers(l1, l2))