class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # trying to brute force to begin with

        max_water = 0
        n = len(heights)

        for i in range(n):
            for j in range(i + 1, n):
                smaller = min(heights[i], heights[j])
                max_water = max(max_water, smaller * (j - i))
        
        return max_water