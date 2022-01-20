# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        count = {}
        p1 = head
        while p1 is not None:
            count[p1] = 1 + count.get(p1,0)
            
            if count[p1] > 1:
                return True
            p1 = p1.next
            
        