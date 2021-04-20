class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Setup: We need - leftmax, rightmax, left pointer, right pointer and area.
        1. We will begin by declaring the variables, which are all 0 except right, which is going to close from the end.
        2. While left < right, we iterate and check our positional index values.
          2.1. If our left value is less than or equal to our right value, we will do the following:
            2.1.1. We will update the leftmax = max(leftmax, value_at_left_index)
            2.1.2. We will add to area: the abs(value_at_left_index - leftmax)
            2.1.3. We will increment the right pointer.
          2.2. If our rught value is smaller than the left, we will do the same as left, but with right values.
            2.2.1. Update rightmax = max(rightmax, value_at_right_index)
            2.2.2. Update the area to the abs(rightmax - value_at_right_index)
            2.2.3. Increment the right pointer.
        3. Return the area.
        '''
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
            