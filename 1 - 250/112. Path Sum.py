# https://leetcode.com/problems/path-sum/description/
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Example 1:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.right = None
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left.left = None
root.right.left.right = None
root.right.right.left = None
root.right.right.right = TreeNode(1)
# targetSum
targetSum = 22
# --- My solution
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        
        remain = targetSum - root.val
        return (
            self.hasPathSum(root.left, remain)
            or
            self.hasPathSum(root.right, remain)
        )
        
# --- Test
sol = Solution()
print(sol.hasPathSum(root, targetSum))