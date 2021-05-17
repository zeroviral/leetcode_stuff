class Solution:  
    def countArrangement(self, N: int) -> int:
        
        self.arrangements = 0
        nums = [N - x for x in range(N)]
            
        def countRecursively(nums, size):

            if size == 1:
                self.arrangements += 1
                return


            for i in range(size):

                if nums[i] % size == 0 or size % nums[i] == 0:

                    tmp = nums[i]
                    nums[i] = nums[0]
                    nums[0] = tmp

                    countRecursively(nums[1:], size - 1)
    
        countRecursively(nums, N)
        
        return self.arrangements