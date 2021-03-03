# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        t = head
        
        ans = []
        
        while t:
            
            ans.append(t.val)
            t = t.next
        
        f = head
        i = 0
        ans.sort()
        while f:
            f.val = ans[i]
            i += 1
            f = f.next
        return head