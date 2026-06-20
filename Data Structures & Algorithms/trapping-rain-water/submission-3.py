# re-solving since last time couldn't figure out what the trick to solving this was

class Solution:
    def trap(self, height: List[int]) -> int:
        # optimal solution since we want to avoid slicing and max computation for every entry

        n = len(height)
        l_max, r_max = [0] * n, [0] * n

        # computing left max for all elements
        curr_l_max = 0 
        for i in range(n):
            l_max[i] = curr_l_max
            curr_l_max = max(curr_l_max, height[i])
        
        # computing right max for all elements
        curr_r_max = 0
        for j in range(n - 1, -1, -1):
            r_max[j] = curr_r_max
            curr_r_max = max(curr_r_max, height[j])
        
        # main pass to compute trapped water
        max_water = 0
        for k in range(n):
            trapped = min(l_max[k], r_max[k]) - height[k]
            
            if trapped > 0:
                max_water += trapped
        
        return max_water