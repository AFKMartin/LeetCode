# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Given the root of a binary tree, return the preorder traversal of its nodes' values.
# Example 1:

# Input: root = [1,null,2,3]
# Output: [1,2,3]
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return
            result.append(node.val)  # root
            dfs(node.left)           # left
            dfs(node.right)          # right

        dfs(root)
        return result

# --- Helper to build tree from list (like LeetCode input)
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            # if the current node is None, just return (base case)
            if node == None:
                return
            # visit the root: add the current node's value to result
            res.append(node.val)

            # recursively visit the left subtree
            dfs(node.left)

            # recursively visit the right subtree
            dfs(node.right)
        # start DFS from the root
        dfs(root)
        # return the final preorder traversal list
        return res

        
# --- Test
if __name__ == "__main__":
    # Example: root = [1, None, 2, 3]
    root = build_tree([1, None, 2, 3])
    sol = Solution()
    print(sol.preorderTraversal(root))  # Expected output: [1, 2, 3]