class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        length = len(heights)
        left = 0
        right = length-1
        areas = []

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            areas.append(height * width)

            if heights[left] <= heights[right]:
                left = left + 1
            else:
                right = right - 1

        return max(areas)

