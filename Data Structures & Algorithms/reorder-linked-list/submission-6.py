# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_ll(self, head: Optional[ListNode]) -> ListNode:
        prev = head
        tmp = head.next

        while tmp:
            nxt = tmp.next

            tmp.next = prev

            # ensure proper null termination
            if prev == head:
                prev.next = None

            prev = tmp

            tmp = nxt
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if (not head.next) or (head and head.next and not head.next.next):
            return
            
        # first finding middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # we want to reverse second half
        reversed_second_half = self.reverse_ll(slow.next)

        # to terminate the 1st list
        slow.next = None

        # maintaining this because this is what we want at the end
        start = head

        t1 = head
        t2 = reversed_second_half

        prev = None
        while t1 and t2:
            t1_next = t1.next
            t2_next = t2.next

            if prev:
                prev.next = t1

            t1.next = t2
            prev = t2

            t1 = t1_next
            t2 = t2_next
        
        if t1:
            prev.next = t1
        elif t2:
            prev.next = t2
        
        head = start