# revisiting: came up with brute force easily, was on right track with trying for either a max heap but realized it 
# won't work so moved in dir of monotonically decreasing queue (had to look syntax up) and was able to implement most
# of it except for having one bug

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # naive: O(n * k) - one main pass thru array extracting windows of size k and finding max

        # heap cannot be really used since need to track window size as well

        if k == 1:
            return nums

        dq = deque()
        left = 0
        res = []

        for right in range(len(nums)):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            
            dq.append(right)

            # one window
            if right - left + 1 == k:
                if dq[0] < left:
                    dq.popleft()
                    
                res.append(nums[dq[0]])
                left += 1

        return res