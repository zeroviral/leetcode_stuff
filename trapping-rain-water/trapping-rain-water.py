class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = rightmax = left = area = 0
        right = len(height) - 1
        
        while left < right:
            if height[left] <= height[right]:
                leftmax = max(leftmax, height[left])
                area += abs(height[left] - leftmax)
                left += 1
            else:
                rightmax = max(height[right], rightmax)
                area += abs(height[right] - rightmax)
                right -= 1
            
        return area
            