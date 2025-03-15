# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return hare

        tortoise = hare = head


        while hare.next and hare.next.next:
            tortoise = tortoise.next
            hare = hare.next.next
        
        return tortoise if not hare.next else tortoise.next