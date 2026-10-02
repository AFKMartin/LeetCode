# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:

# Input: root = [1,null,2,3]
# Output: [3,2,1]
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node):
            if not node:
                return
            result.append(node.val) # root
            dfs(node.right)         # left
            dfs(node.right)         # right
        
        dfs(root)
        return result
    
# --- Helper to build tree from list (Wait this looks familiar)
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:

    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root
# --- My solution
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            # if the current node is None, just return (base case)
            if node == None:
                return
            # postorder means = left -> right -> root
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        
        dfs(root)
        return res
      
# --- Test
if __name__ == "__main__":
    # Example: root = [1, None, 2, 3]
    root = build_tree([1, None, 2, 3])
    sol = Solution()
    print(sol.postorderTraversal(root))  # Expected output: [3, 2, 1]