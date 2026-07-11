# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # very 1st element
        prev = head

        # 2nd element
        start = head.next

        while start:
            nxt = start.next

            start.next = prev
            if prev == head:
                prev.next = None
            
            prev = start

            start = nxt
        
        return prev
        
        return prev