class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
#how to run start
#subarraySum([1,1,1], 2)
#how to run end

    
#first we start from a sum which is equal to 0, and the count of it is 1. 
# this is the input list ex :   [1 4 9 -5 8]
# this is the sum array (s) ex : [0  1    5    13    8    16 ]    
    
        sumDict = {0:1}
        n = len(nums)
        count = 0 
        s = 0 

        for num in nums:
    #we keep adding to the cumilative sums, s:         
            s += num

    #we make sure to check if the sum - k is already in the dictionary, if so, increase the count.         
            if s-k in sumDict:
                count += sumDict[s-k]

    #we check if s is already in the sumDict, if so, increase by 1, if not assign 1.             
            if s in sumDict:
                sumDict[s] +=1
            else:
                sumDict[s] = 1

    #finally return the occurance    
        return count