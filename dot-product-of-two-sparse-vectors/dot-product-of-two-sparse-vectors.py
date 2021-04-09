class SparseVector:
    def __init__(self, nums: List[int]):
        # self.nums = nums
        self.vector = {i : element for i, element in enumerate(nums) if element > 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        finalSum = 0
        
        for key, value in vec.vector.items():
            if key in self.vector:
                finalSum += (self.vector[key] *  value)
        return finalSum

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)