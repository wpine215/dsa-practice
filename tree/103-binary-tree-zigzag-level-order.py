# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# BFS template based off https://emre.me/coding-patterns/breadth-first-search/

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS to get level-ordering, then keep track of level and reverse every other level output
        result = []
        if root is None:
            return result
        
        queue = deque()
        queue.append(root)
        
        leftToRight = True
        
        while queue:
            level_size = len(queue)
            current_level_elements = []
            
            for _ in range(level_size):
                current_node = queue.popleft()
                current_level_elements.append(current_node.val)
                
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                
            if leftToRight:
                result.append(current_level_elements)
            else:
                result.append(current_level_elements[::-1])
            
            leftToRight = not leftToRight
            
        return result
