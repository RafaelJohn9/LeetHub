# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head.next
        sub_result = []
        new_head = ListNode()
        temp_for_new_head = new_head

        while temp:
            if temp.val == 0:
                temp_for_new_head.next = ListNode()
                temp_for_new_head = temp_for_new_head.next
                temp_for_new_head.val = sum(sub_result)
                sub_result = []
            else:
                sub_result.append(temp.val)
            temp = temp.next
        

        return new_head.next
        