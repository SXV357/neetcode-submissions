# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        k = len(lists)
        t1 = lists[0]

        for i in range(1, k):
            t2 = lists[i]

            dummy = ListNode() # value of 0, next = None
            tail = dummy

            while t1 and t2:
                val_one, val_two = t1.val, t2.val

                if val_one <= val_two:
                    tail.next = t1

                    t1 = t1.next
                else:
                    tail.next = t2

                    t2 = t2.next
                
                tail = tail.next
            
            if not t1:
                tail.next = t2
            elif not t2:
                tail.next = t1
            
            # need to save head of merged list for next iteration
            t1 = dummy.next
        
        return t1
