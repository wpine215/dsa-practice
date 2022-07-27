# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# NAIVE SOLUTION
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         return self.maxDepthHelper(root, 1)
        
#     def maxDepthHelper(self, root, maxSoFar):
#         m = maxSoFar
#         if root.left:
#             m = max(m, self.maxDepthHelper(root.left, maxSoFar + 1))
#         if root.right:
#             m = max(m, self.maxDepthHelper(root.right, maxSoFar + 1))
#         return m

# OPTIMIZED SOLUTION
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.maxDepthHelper(root, 1)
        
    def maxDepthHelper(self, root, maxSoFar):
        m = maxSoFar
        if root.left:
            m = max(m, self.maxDepthHelper(root.left, maxSoFar + 1))
        if root.right:
            m = max(m, self.maxDepthHelper(root.right, maxSoFar + 1))
        return m
