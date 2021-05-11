class Solution:
    def isHappy(self, n: int) -> bool:
        
        def calculateNext(n):
            
            transposeArr = "".join(str(n))
            
            temp = []
            
            for val in transposeArr:
                temp.append(int(val) ** 2)
            
            return sum(temp)
        
        lookup = set()
        
        while n != 1:
            n = calculateNext(n)
            
            if n in lookup:
                return False
            else:
                lookup.add(n)
        return True