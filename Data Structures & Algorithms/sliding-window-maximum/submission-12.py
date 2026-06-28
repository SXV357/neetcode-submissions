from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
            
        dq = deque()

        res = []
        left = 0

        for right in range(len(nums)):
            curr = nums[right]
            while dq and nums[dq[-1]] < curr:
                dq.pop()
            
            dq.append(right)

            # hit a window of size k so update res w curr max
            if right - left + 1 == k:
                if dq[0] < left:
                    dq.popleft()

                res.append(nums[dq[0]])
                left += 1

        
        return res