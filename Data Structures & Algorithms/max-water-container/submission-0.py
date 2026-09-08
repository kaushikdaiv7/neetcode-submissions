class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_water = -1

        left, right = 0, n-1

        while left < right:
            breadth = right - left
            height = min(heights[left], heights[right])
            water_store = breadth * height
            max_water = max(water_store, max_water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water
        