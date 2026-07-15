# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_ll(self, head: Optional[ListNode]) -> ListNode:
        if not head:
            return 
            
        prev = head
        temp = head.next

        while temp:
            nxt = temp.next

            temp.next = prev
            if prev == head:
                prev.next = None

            prev = temp

            temp = nxt
        
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rev = self.reverse_ll(head)

        cnt = 0
        temp, prev = rev, None

        while temp:
            cnt += 1

            if cnt == n:
                if prev:
                    prev.next = temp.next
                    break
                # handle the case where its just length of 1 and n == 1
                else:
                    rev = rev.next
                    break
            
            prev = temp
            temp = temp.next
        
        modified = self.reverse_ll(rev)
        return modified