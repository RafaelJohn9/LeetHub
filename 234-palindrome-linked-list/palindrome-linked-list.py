# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        linked_list = []

        while head:
            linked_list.append(head.val)
            head = head.next
        
        left = 0
        right = len(linked_list) - 1

        while left < right:
            if linked_list[left] != linked_list[right]:
                return False
            
            left += 1
            right -= 1
        
        return True