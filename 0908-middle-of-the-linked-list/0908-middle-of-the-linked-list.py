# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_len = 0

        iter_node = head
        while iter_node:
            list_len += 1
            iter_node = iter_node.next
        
        mid = list_len // 2 + 1

        count = 1
        iter_node = head
        while count != mid:
            iter_node = iter_node.next
            count += 1

        return iter_node
