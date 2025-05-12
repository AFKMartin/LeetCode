# https://leetcode.com/problems/merge-two-sorted-lists/
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# From python list to linked list
def ToLinkedList(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# A way to print the Linked list to check output
def PrintLinkedList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# --- My solution
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        sol = dummy

        while list1 and list2:
            if list1.val < list2.val:
                sol.next = list1
                list1 = list1.next
            else:
                sol.next = list2
                list2 = list2.next
            sol = sol.next

        sol.next = list1 if list1 else list2
        return dummy.next
# --- Test
list1 = ToLinkedList([1,2,4])
list2 = ToLinkedList([1,3,4])

sol = Solution()
merged = sol.mergeTwoLists(list1, list2)
PrintLinkedList(merged)

    
        
        


        