# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # def rotate receives head
        # find len of list
        # use while loop to rotate k % len_list times

        if not head or k == 0:
            return head     

        def rotate(head):
            temp = head
            prev = None
            prev_prev = None

            while temp:
                prev_prev = prev
                prev = temp
                temp = temp.next
            
            if prev_prev and prev:
                prev_prev.next = None
                prev.next = head
                head = prev
        
            return head

        
        # list len
        list_len = 0
        temp = head

        while temp:
            list_len += 1
            temp = temp.next

        i = 0
        while i < (k % list_len):
            head = rotate(head)
            i += 1
        
        return head
