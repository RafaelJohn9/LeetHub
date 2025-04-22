# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_l1 = l1
        head_l2 = l2

        first_num = ""
        while head_l1:
            first_num += str(head_l1.val)
            head_l1 = head_l1.next
        
        second_num = ""
        while head_l2:
            second_num += str(head_l2.val)
            head_l2 = head_l2.next
        
        first_num = int(first_num[::-1])
        second_num = int(second_num[::-1])

        nums = list(str(first_num + second_num))

        n = len(nums)
        j = n - 1

        result = ListNode()
        result.val = int(nums[j])
        j -= 1
        head = result
        while j >= 0:
            new_node = ListNode()
            result.next = new_node
            result = result.next
            result.val = int(nums[j])
            j -= 1
        
        return head