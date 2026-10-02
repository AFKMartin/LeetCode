# https://leetcode.com/problems/binary-tree-inorder-traversal/
# 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# root = [1,null,2,3]
root = TreeNode(1)
# root.left = None  
root.right = TreeNode(2)
root.right.left = TreeNode(3)
# --- My solution
class Solution:
    def inorderTraversal(self, root):
        c = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            c.append(node.val)
            dfs(node.right)
        dfs(root)      
        return c
# --- Test
sol = Solution()
print(sol.inorderTraversal(root))

 
