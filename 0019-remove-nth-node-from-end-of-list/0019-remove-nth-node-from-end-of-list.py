# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find the length of the list
        # Move to the specific point
        # if prev node and prev.next to curr.next else curr.next

        len_of_linked_list = 0
        temp = head

        while temp:
            len_of_linked_list += 1
            temp = temp.next
        

        curr = head
        prev = None
        i = 0
        while curr:
            if len_of_linked_list - n == i:
                if prev:
                    prev.next = curr.next
                    return head
                else:
                    return curr.next
            
            prev = curr
            curr = curr.next
            i += 1
        
        return None