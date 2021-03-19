class Solution:
    def countBits(self, num: int) -> List[int]:
        
        ans = []
        
        for i in range(num + 1):
            
            binary = bin(i)
            val = len([ones for ones in binary[2:] if ones=='1'])
            ans.append(val)
            
        return ans