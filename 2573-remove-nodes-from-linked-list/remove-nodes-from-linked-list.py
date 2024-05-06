# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNode(self, head: Optional[ListNode], node: Optional[ListNode]) -> Optional[ListNode]:
        """deletes node appropriately and returns previous node
        if null, returns next node of the deleted node """

        if not node or not head:
            return
        
        prev_node = None
        curr_node = head

        while curr_node.val != node.val:
            prev_node = curr_node

            # if node does not exist
            if not curr_node.next:
                return None

            curr_node = curr_node.next
        
        if not prev_node:
            return curr_node.next

        prev_node.next = curr_node.next
        return prev_node

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ removes nodes from linked list if right node has greater value than it"""
        backtrack = []
        prev_node = None
        curr_node = head

        while curr_node:
            if curr_node.val > head.val:
                head = curr_node
            if curr_node.next and curr_node.next.val > curr_node.val:
                if not prev_node:
                    head = curr_node = curr_node.next
                    continue
                curr_node = self.deleteNode(prev_node, curr_node)
                backtrack.pop()
                prev_node = backtrack[-1] if len(backtrack) != 0 else None
            else:
                prev_node = curr_node
                backtrack.append(prev_node)
                curr_node = curr_node.next
        return head

