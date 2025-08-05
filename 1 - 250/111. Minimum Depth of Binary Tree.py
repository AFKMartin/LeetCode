# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# root = [3,9,20,null,null,15,7]
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
    def minDepth(self, root) -> int:
        if not root:
            return 0
        
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
# --- Test
sol = Solution()
print(sol.minDepth(root))     


