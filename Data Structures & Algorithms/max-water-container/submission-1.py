class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # trying to brute force to begin with

        max_water = 0
        i, j = 0, len(heights) - 1

        while i < j:
            max_water = max(max_water, (j - i) * min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_water