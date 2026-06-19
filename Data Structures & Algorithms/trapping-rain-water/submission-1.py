class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)

        l_max_prefix = [0] * n
        r_max_prefix = [0] * n

        l_max = 0
        # to populate l_max_prefix first
        for i in range(n):
            l_max_prefix[i] = l_max
            l_max = max(l_max, height[i])
        
        r_max = 0
        # to populate r_max_prefix first
        for i in range(n - 1, -1, -1):
            r_max_prefix[i] = r_max
            r_max = max(r_max, height[i])
        
        for j in range(n):
            computed_water = min(l_max_prefix[j], r_max_prefix[j]) - height[j]
            if computed_water > 0: 
                max_water += computed_water
        
        return max_water