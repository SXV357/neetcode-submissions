# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        if list1 and not list2:
            return list1
        
        if not list1 and list2:
            return list2
        
        t1 = list1
        t2 = list2

        # what we will be returning at the end
        start = None
        if t1 and t2:
            if t1.val <= t2.val:
                start = t1
            else:
                start = t2

        prev = None

        while t1 and t2:
            t1_next = t1.next
            t2_next = t2.next

            t1_val = t1.val
            t2_val = t2.val

            if t1_val == t2_val:
                # will need the connection from before to happen
                if prev:
                    prev.next = t1

                t1.next = t2
                prev = t2

                # only if they're equal we will move both forward similar to 2 pointers
                t1 = t1_next
                t2 = t2_next
            elif t1_val < t2_val:
                if prev:
                    prev.next = t1
                
                prev = t1
                t1 = t1_next
            else:
                if prev:
                    prev.next = t2
                
                prev = t2
                t2 = t2_next
        
        # exhaust both lists now
        temp2 = t2
        while temp2:
            if prev:
                prev.next = temp2
                
            prev = temp2
            temp2 = temp2.next
        
        temp1 = t1
        while temp1:
            if prev:
                prev.next = temp1

            prev = temp1 
            temp1 = temp1.next
        
        if prev:
            prev.next = None
        
        return start