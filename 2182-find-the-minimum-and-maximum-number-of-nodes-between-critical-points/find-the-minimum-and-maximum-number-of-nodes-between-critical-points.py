# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        tail = head
        body = head.next if head.next else None
        head =  body.next if body else None
        i = 1

        # [[index from 1]]
        critical_point = []

        while head:
            if body.val < tail.val and body.val < head.val:
                critical_point.append(i)
            elif body.val > tail.val and body.val > head.val:
                critical_point.append(i)
            
            i += 1
            head = head.next
            body = body.next
            tail = tail.next
        
        if len(critical_point) < 2:
            return [-1, -1] 
        
        max_num = critical_point[-1]
        min_num = critical_point[0]

        min_distance = (max_num - min_num)

        for i in range(1, len(critical_point)):
            if (critical_point[i] - critical_point[i - 1]) < min_distance:
                min_distance = critical_point[i] - critical_point[i - 1]


        return [min_distance, (max_num - min_num)]