class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = second_smallest = float('inf')
        
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= second_smallest:
                second_smallest = num
                # We found the third smallest number, therefore return true cause there's a increasing triplet sequence
            else:
                return True
        
        return False