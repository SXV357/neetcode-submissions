class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0

        for i in range(len(height)):
            left = height[:i]
            right = height[i + 1:]

            max_l, max_r = max(left) if len(left) > 0 else 0, max(right) if len(right) > 0 else 0
            water = min(max_l, max_r) - height[i]

            if water >= 0:
                max_water += water
        
        return max_water