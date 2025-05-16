# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        tortoise = head
        hare = head
        meeting_node = None

        while hare.next and hare.next.next:
            hare = hare.next.next
            tortoise = tortoise.next

            if tortoise == hare:
                meeting_node = hare
                break


        tortoise = head
        while meeting_node:
            if tortoise == meeting_node:
                return tortoise
            
            meeting_node = meeting_node.next
            tortoise = tortoise.next
            
        
        return None