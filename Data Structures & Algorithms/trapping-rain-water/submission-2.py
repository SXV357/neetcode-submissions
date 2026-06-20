# re-solving since last time couldn't figure out what the trick to solving this was

class Solution:
    def trap(self, height: List[int]) -> int:
        # brute force to begin with
        # we want to calculate how much water can go above each bar and we add all up

        max_water = 0
        for i in range(len(height)):
            # grab all the bars to the left of the current one and to right of current one
            left = height[:i]
            right = height[i+1:]

            # max height of a bar to left of current one and to right of current one
            l_max = 0 if len(left) == 0 else max(left)
            r_max = 0 if len(right) == 0 else max(right)

            # idea is that finding 2 tallest bars on either side helps ensure that for water
            # to go above a bar it is trapped (#1). then how high water can go will be based on
            # which of the 2 tallest bars is shorter otherwise we risk spilling. then finally
            # we need to subtract the current height because if the bar already has some non-zero
            # height that itself takes up space and we just care about how much water goes
            # on top
            trapped_water = min(l_max, r_max) - height[i]
            
            if trapped_water > 0:
                max_water += trapped_water
        
        return max_water