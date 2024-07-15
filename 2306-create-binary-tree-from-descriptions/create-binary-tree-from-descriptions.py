# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        is_child = {}
        trees = {}

        for parent, child, is_left in descriptions:
            if parent not in trees:
                trees[parent] = TreeNode(val=parent)
            if child not in trees:
                trees[child] = TreeNode(val=child)
            
            if is_left:
                trees[parent].left = trees[child]
            else:
                trees[parent].right = trees[child]
            
            is_child[child] = parent

        # Find the root node, which is not a child of any other node
        for node in trees:
            if node not in is_child:
                return trees[node]

        return None