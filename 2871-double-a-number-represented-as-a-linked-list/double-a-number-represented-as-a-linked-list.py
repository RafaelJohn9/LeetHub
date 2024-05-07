# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import sys
        sys.set_int_max_str_digits(20000)

        double_number = ""
        curr_node = head

        while curr_node:
           double_number += str(curr_node.val)
           curr_node = curr_node.next

        double_number = int(double_number) * 2
        double_number = str(double_number)
        double_number = list(double_number)

        new_node_head = ListNode()
        curr_node = new_node_head
        first = True

        while len(double_number) > 0:
            if not first:
                curr_node.next = ListNode()
                curr_node = curr_node.next

            curr_node.val = double_number[0]
            del(double_number[0])
            first = False
        
        return new_node_head