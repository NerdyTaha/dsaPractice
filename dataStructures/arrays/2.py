class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        #until the middle, to maximise area
        while left < right:
            width = right - left
            current_height = min(height[left],height[right])
            current_area = current_height * width
            if current_area > max_area:
                max_area = current_area 
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area