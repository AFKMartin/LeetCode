# https://leetcode.com/problems/merge-k-sorted-lists/description/
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val}->{self.next}"
# --- My solution
import heapq
class Solution:
    def mergeKLists(self, lists):
        heap = []
        
        # Initialize heap with the first node of each list
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))  # (value, index, node)
        
        c = ListNode(0)
        curr = c
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return c.next
# --- Helper
def build_linked_list(arr):
    c = ListNode(0)
    curr = c
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return c.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
# --- Test
lists = [[1,4,5],[1,3,4],[2,6]]
linked_lists = [build_linked_list(l) for l in lists]

sol = Solution()
merged = sol.mergeKLists(linked_lists)

print(linked_list_to_list(merged))