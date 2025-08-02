# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
# Example 1:

# Input: head = [1,1,2]
# Output: [1,2]
head = [1,1,2]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next        
# --- My solution
class Solution:
    def deleteDuplicates(self, head):
        c = head
        while c and c.next:
            if c.val == c.next.val:
                c.next = c.next.next  
            else:
                c = c.next
        return head
# --- Test
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

head = build_linked_list([1, 1, 2])
sol = Solution()
new_head = sol.deleteDuplicates(head)
print(linked_list_to_list(new_head))