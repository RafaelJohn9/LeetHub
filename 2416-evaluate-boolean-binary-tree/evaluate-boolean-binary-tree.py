# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: TreeNode) -> bool:
        if root.val == 0:
            return False
        if root.val == 1:
            return True
        
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        
        if root.val == 2:  # OR operation
            return left_val or right_val
        elif root.val == 3:  # AND operation
            return left_val and right_val