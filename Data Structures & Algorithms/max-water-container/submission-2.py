# coming back to resolve since couldn't come up with optimal 2-ptr solution 1st time around

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_water = 0
        while l < r:
            # height of container is constrained by smaller height
            # width is just how far apart in the array itself
            stored = min(heights[l], heights[r]) * (r - l)
            max_water = max(max_water, stored)

            # idea is if height on this side is small but we move the other pointer
            # inward, we decrease distance but height is still constrained by smaller one
            # we'd rather keep the other pointer at the larger height and move the pointer
            # at the smaller height inward to try for a bigger value
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_water