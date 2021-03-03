# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        t1, t2 = l1, l2
        
        if l1 is None or l2 is None:
            return l1 or l2
        
        if l1.val < l2.val:
            dummy = ListNode(l1.val)
            t1 = t1.next
        else:
            dummy = ListNode(l2.val)
            t2 = t2.next
        
        head = dummy
        
        while t1 and t2:
            
            if t1.val < t2.val:
                head.next = t1
                head = head.next
                t1 = t1.next
            else:
                head.next = t2
                head = head.next
                t2 = t2.next
        
        if t1:
            head.next = t1
        else:
            head.next = t2
        
        return dummy
            