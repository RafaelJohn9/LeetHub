# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # find the length to the end
        iter_node = node
        length_from_node = 0
        while iter_node.next:
            length_from_node += 1
            iter_node = iter_node.next
        
        # delete the node
        i = 0
        while i < length_from_node - 1:
            node.val = node.next.val
            node = node.next
            i += 1
        
        node.val = node.next.val
        node.next = None
        