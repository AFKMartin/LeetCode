# https://leetcode.com/problems/balanced-binary-tree/description/
# Given a binary tree, determine if it is height-balanced.
# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: true

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
    def isBalanced(self, root):
        def test(node):
            if not node:
                return 0
            
            left = test(node.left)
            if left == -1: 
                return -1 # left not balanced
            
            right = test(node.right)
            if right == -1:
                return -1 # right not balanced
            
            if abs(left - right) > 1:
                return -1 # current node not balanced
            
            return max(left, right) + 1
        return test(root) != -1 
# --- Test
sol = Solution()
print(sol.isBalanced(root))