class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        lookup = set()
        
        curr = headA
        while curr:
            
            lookup.add(curr)
            curr = curr.next
        
        curr = headB
        while curr:
            
            if curr in lookup:
                return curr
            curr = curr.next
        
        return None