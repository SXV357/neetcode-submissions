# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Tuple

class Solution:
    def find_tail(self, head: Optional[ListNode]) -> Tuple[ListNode, ListNode]:
        temp = head
        prev = None
        
        while temp:
            if not temp.next:
                break
            
            prev = temp
            temp = temp.next
        
        return (prev, temp)

    def reorderList(self, head: Optional[ListNode]) -> None:
        # # lists of length 1 (min length possible) and 2 (trivial)
        # if (not head.next) or (head and head.next and not head.next.next):
        #     return head
        
        # we care about this
        start = head
        
        # what we will be using for modifications and stuff internally
        temp = head
        prev = None
        
        while temp.next is not None:
            tail_prev, tail = self.find_tail(temp)
            
            nxt = temp.next
            if prev:
                prev.next = temp
            
            temp.next = tail
            prev = tail
            
            if tail != nxt:
                tail_prev.next = None

            temp = nxt
        
        if prev:
            prev.next = temp
            temp.next = None
        
        
        head = start