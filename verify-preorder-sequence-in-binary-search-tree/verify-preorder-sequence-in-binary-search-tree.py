class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        peek, stack = None, []
        for element in preorder:
            while stack and element > stack[-1]:
                peek = stack.pop()
            if peek and element < peek:
                return False
            stack.append(element)   
        return True