# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_ll(self, head: Optional[ListNode]):
        prev = head
        temp = head.next

        while temp:
            nxt = temp.next

            temp.next = prev

            # properly terminate reversed list (only valid for this case)
            if prev == head:
                prev.next = None

            prev = temp
            temp = nxt
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or head and not head.next:
            return

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
                
        # now slow will point to middle of the list
        t2 = self.reverse_ll(slow.next)

        # terminate the first list at slow
        slow.next = None

        t1 = head
        t1_copy = head

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

        if not t1:
            prev.next = t2
        elif not t2:
            prev.next = t1
        
        head = t1_copy