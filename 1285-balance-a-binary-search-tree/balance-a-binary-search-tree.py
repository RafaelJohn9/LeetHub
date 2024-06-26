# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """ Balances a BST """
        def findValues(root: TreeNode) -> List[int]:
            """ maps values of a BST in a list """
            if not root:
                return []
            return findValues(root.left) + [root.val] + findValues(root.right)
        
        def createTree(values: List[int]) -> TreeNode:
            if not values:
                return None
            
            mid = len(values) // 2
            root = TreeNode(values[mid])
            root.left = createTree(values[:mid])
            root.right = createTree(values[mid + 1:])
            return root

        values = findValues(root)
        return createTree(values)