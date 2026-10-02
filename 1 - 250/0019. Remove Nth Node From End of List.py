# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# --- My solution
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        c = ListNode(0, head)
        fast = slow = c

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers until fast reaches end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the target node
        slow.next = slow.next.next

        return c.next
    
# --- Test
def list_to_linkedlist(lst):
    c = ListNode()
    curr = c
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return c.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

head = list_to_linkedlist([1, 2, 3, 4, 5])
n = 2
sol = Solution()
new_head = sol.removeNthFromEnd(head, n)
print(linkedlist_to_list(new_head))  
