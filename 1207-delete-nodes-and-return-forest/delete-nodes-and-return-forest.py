# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # map to_delete
        to_delete_dict: dict = {val: 1 for val in to_delete}

        result:List = []

        def forestMapper(node: TreeNode, result: List, to_delete_dict: dict) -> None:
            """ Maps the forest """
            if node.right:
                forestMapper(node.right, result, to_delete_dict)
                if node.right.val == -1:
                    node.right = None

            if node.left:
                forestMapper(node.left, result, to_delete_dict)

                if node.left.val == -1:
                    node.left = None

            if to_delete_dict.get(node.val, 0):
                node.val = -1

                if node.right:
                    result.append(node.right)
                if node.left:
                    result.append(node.left)

        forestMapper(root, result, to_delete_dict)

        if root.val != -1:
            result.append(root)

        return result