# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = None, head
        while p2 is not None:
            p3 = p2.next # Take the next node and keep it
            p2.next = p1 # Reverse the current node
            p1 = p2 # move the pointer left 
            p2 = p3 #move the pointer left
        return p1
        
        