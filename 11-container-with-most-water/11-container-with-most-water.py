class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left_ptr = 0 # Left pointer initialize to left most index
        right_ptr = n - 1 # Right pointer initialize to right most index
        
        # Formula to calculate resultant water for particular selection of left and right pointer is
        # Water contained = minimum of left and right height multiplied by difference between right and left
        result = min(height[left_ptr],height[right_ptr]) * (right_ptr - left_ptr)
        
        while left_ptr <= right_ptr:
            # Move left pointer when left is smaller then right
            if height[left_ptr] < height[right_ptr]: 
                left_ptr += 1
            else:
                right_ptr -= 1
            result = max(result, min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr))
            
        return result