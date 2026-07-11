# revisiting this since I couldn't figure it out the 1st time

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 9999

        l, r = 0, len(nums) - 1

        # trivial case: array is already sorted so just return 1st element
        if nums[l] <= nums[r]:
            return nums[l]

        while l <= r:
            # the middle element could end up being the smallest one so we update it
            # based on the calculated mid
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return res