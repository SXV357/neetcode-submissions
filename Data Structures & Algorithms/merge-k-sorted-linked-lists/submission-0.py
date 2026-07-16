# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force - throw everything into min heap then connect them

        heap = []
        for head in lists:
            temp = head

            while temp:
                heapq.heappush(heap, temp.val)
                temp = temp.next
        
        if not heap:
            return None
        
        sorted_li = []
        initial = ListNode(heapq.heappop(heap))
        
        prev = initial

        while heap:
            nxt = ListNode(heapq.heappop(heap))
            prev.next = nxt

            prev = nxt
        
        return initial
