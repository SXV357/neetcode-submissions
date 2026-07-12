# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # O(n) space solution to begin with just for a baseline

        elems = []
        temp = head

        while temp:
            elems.append(temp)
            temp = temp.next
        
        l, r = 0, len(elems) - 1
        prev = None

        while l <= r:
            curr_l = elems[l]
            curr_r = elems[r]

            if prev:
                prev.next = curr_l

            if curr_l != curr_r:
                curr_l.next = curr_r

            prev = curr_r

            l += 1
            r -= 1
        
        if prev:
            prev.next = None
            
        head = elems[0]