# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        tortoise = hare = head

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                break
        else:
            return None

        tortoise = head
        while tortoise != hare:
            hare = hare.next
            tortoise = tortoise.next
            
        
        return hare