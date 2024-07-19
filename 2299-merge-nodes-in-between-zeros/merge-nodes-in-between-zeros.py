# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        results = []
        start = 0
        end = 0
        temp = head.next

        sub_result = []
        while temp:
            if temp.val == 0:
                results.append(sub_result)
                sub_result = []
            else:
                sub_result.append(temp.val)
            temp = temp.next
        
        new_head = ListNode(val=sum(results[0]))
        temp = new_head
        for new_val in results[1:]:
            temp.next = ListNode()
            temp = temp.next
            temp.val = sum(new_val)

        return new_head
        