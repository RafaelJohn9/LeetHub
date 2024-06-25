# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.summation = 0
        
        def depthFirstSearch(node):
            """ Recursively goes through the binary search tree """
            if not node:
                return
            
            # Traverse right subtree first (greater values)
            if node.right:
                depthFirstSearch(node.right)
                
            # Update the current node's value
            self.summation += node.val
            node.val = self.summation
            
            # Traverse left subtree
            if node.left:
                depthFirstSearch(node.left)
        
        depthFirstSearch(root)
        return root
