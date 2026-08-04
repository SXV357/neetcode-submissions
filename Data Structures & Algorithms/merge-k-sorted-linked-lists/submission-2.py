# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        t1 = lists[0]

        for i in range(1, len(lists)):
            dummy = ListNode()
            tail = dummy

            t2 = lists[i]

            while t1 and t2:
                t1_val, t1_next = t1.val, t1.next
                t2_val, t2_next = t2.val, t2.next

                if t1_val <= t2_val:
                    tail.next = t1
                    tail = t1

                    t1 = t1_next
                else:
                    tail.next = t2
                    tail = t2

                    t2 = t2_next
            
            if not t1:
                tail.next = t2
            elif not t2:
                tail.next = t1
            
            t1 = dummy.next
        
        return t1
