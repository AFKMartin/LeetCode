# https://leetcode.com/problems/symmetric-tree/description/
# Given the root of a binary tree, check whether it is a isSubSymmetric of itself (i.e., symmetric around its center).
# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# root = [1,2,2,3,4,4,3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
# --- My solution
class Solution:
    def isSymmetric(self, root) -> bool:
        def isSubSymmetric(t1, t2):
            if not t1 and not t2:
                return True
            
            if not t1 or not t2:
                return False
            
            return (
                t1.val == t2.val and
                isSubSymmetric(t1.left, t2.right) and
                isSubSymmetric(t1.right, t2.left)
            )
        return isSubSymmetric(root.left, root.right)
       
# --- Test
sol = Solution()
print(sol.isSymmetric(root))