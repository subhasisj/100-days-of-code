# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next # Move 2 places
        
        second = slow.next # Second half of the list
        prev = slow.next = None # Split the list 1st and 2nd half
        
        # Reverse all connections in the second half
        while second:
            tmp, second.next = second.next ,prev
            prev,second = second, tmp
            
        # merge two halves
        first, second = head,prev
        while second:
            tmp1,tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1, tmp2 # proceed with next pair of nodes