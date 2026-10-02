# https://leetcode.com/problems/linked-list-cycle/description/
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
head = [3,2,0,-4]
pos = 1
# --- ListNode Class
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

# From Python list → Linked list
def ToLinkedList(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# From Python list → Linked list with cycle
# pos = index of node where the tail should connect, or -1 for no cycle
def ToLinkedListWithCycle(lst, pos):
    if not lst:
        return None
    dummy = ListNode(0)
    current = dummy
    nodes = []
    for val in lst:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
    if pos != -1:
        current.next = nodes[pos]  # create cycle
    return dummy.next

# Convert Linked list → Python list (safe for no cycles)
def LinkedListToList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Print Linked list (safe version, stops if cycle detected)
def PrintLinkedList(head, limit=50):
    result = []
    count = 0
    while head and count < limit:
        result.append(str(head.val))
        head = head.next
        count += 1
    if head:  # stopped because of limit, likely a cycle
        result.append("...")
    print("->".join(result) if result else "Empty list")

head = ToLinkedListWithCycle([3,2,0,-4], 1)
# --- My solution
class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if fast == None or fast.next == None:
                # return False
            if slow == fast:
                return True
        return False
# --- Test
sol = Solution()
print(sol.hasCycle(head))
