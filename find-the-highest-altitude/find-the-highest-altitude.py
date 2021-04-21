class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        '''
        1. We need: currSum, maxSum
        2. Iterate through gain list and keep track of the cumulative sum. 
            2.1. maxSum = max(maxSum, currSum)
        '''
        
        currSum = 0
        maxSum = 0
        
        for element in gain:
            currSum += element
            maxSum = max(maxSum, currSum)
        return maxSum
        
        