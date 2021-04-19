class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        '''
        1. We need: l pointer, count, maxLength
        2. Iterate through the array using a left/right pointer method, and count zeroes.
            2.1. Once our count reaches the allowed zeroes, (K from input) then we move left pointer up.
                2.1.1. When we hit our inner while loop to move left up, we check the left pointer index and see if it is 0.
                    2.1.1.1. If we have a zero at the left pointer, we remove 1 from count before incrementing left pointer.
            2.2. Take the max(maxLength, r - l + 1)
        3. Return our maxLength
                    
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] = maxLength = 6 (ans)
                        l
                                       r
        '''
        l = count = maxLength = 0
        for r in range(len(A)):
            if A[r] == 0:
                count += 1
            
            while l <= r and count > K:
                if A[l] == 0:
                    count -= 1
                l += 1
            
            maxLength = max(maxLength, r - l + 1)
        return maxLength
        
            