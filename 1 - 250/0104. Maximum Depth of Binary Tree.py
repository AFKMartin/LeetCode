# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# root = [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = None
root.left.right = None
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
# --- My solution
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
# --- Test
sol = Solution()
print(sol.maxDepth(root))