# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0, None)
        after_head = ListNode(0, None)

        temp_before = before_head
        temp_after = after_head

        while head:
            if head.val < x:
                temp_before.next = head
                temp_before = temp_before.next
            else:
                temp_after.next = head
                temp_after = temp_after.next
            
            head = head.next
        
        temp_before.next = after_head.next
        temp_after.next = None

        return before_head.next

