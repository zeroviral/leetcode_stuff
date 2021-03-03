class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        ans = []
        
        for element in S:
            # If stack not empty and top element is the same as our current element, pop it off
            if ans and ans[-1] == element:
                ans.pop()
            else:
                ans.append(element)
                
        return "".join(ans)