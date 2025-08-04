# https://leetcode.com/problems/same-tree/description/
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# p = [1,2,3], q = [1,2,3]
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
# --- My solution
class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        return (
            p.val == q.val and
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )
# --- Test
sol = Solution()
print(sol.isSameTree(p,q))