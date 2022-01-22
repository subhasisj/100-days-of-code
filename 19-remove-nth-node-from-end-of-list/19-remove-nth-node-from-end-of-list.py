# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        p1, p2 = dummy,head
        
     
        node_distance = 0
        while node_distance < n and p2:
            node_distance+=1
            p2 = p2.next
        
#         if p2 is None:
#             head.value = head.next.value
#             head.next = head.next.next
#             return head
        while p2:
            p1 = p1.next
            p2 = p2.next
            
        p1.next = p1.next.next
            
        return dummy.next