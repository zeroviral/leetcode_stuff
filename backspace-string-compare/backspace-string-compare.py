class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        stack = []
        finalT = ""
        finalS = ""
        
        for element in S:
            if element == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(element)
                
        
        finalS = "".join(stack)
        
        stack = []
        
        for element in T:
            if element == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(element)
            
        finalT = "".join(stack)
        print(finalS, finalT)
        
        
        return finalS == finalT
                