# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # BASE CASE
        if root is None:
            return None
        
        # RECURSIVE CASE
        left_node = self.removeLeafNodes(root.left, target)
        right_node = self.removeLeafNodes(root.right, target)

        if root.left and root.left.val is None:
            root.left = None

        if root. right and root.right.val is None:
            root.right = None
        
        if not root.left and not root.right and root.val == target:
            root.val = None
        
        
        if root.val:
            return root
        else:
            None