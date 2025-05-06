# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # make a circular list
        # cut it where it is needed

        if not head or k == 0:
            return head
        
        # make a circular list
        len_list = 0
        prev = None
        temp = head
        while temp:
            len_list += 1
            prev = temp
            temp = temp.next
        
        prev.next = head


        # cut it where needed
        real_k = k % len_list
        next_head_index = len_list - real_k
        prev = None
        temp = head
        i = 0

        while i < next_head_index:
            prev = temp
            temp = temp.next
            i += 1
        
        prev.next = None
        return temp
