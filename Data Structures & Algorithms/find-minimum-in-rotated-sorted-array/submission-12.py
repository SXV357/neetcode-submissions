class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = 9999

        l, r = 0, len(nums) - 1

        # that means already sorted so return leftmost element
        if nums[l] <= nums[r]:
            return nums[l]

        while l <= r:
            m = (l + r) // 2

            # edge case to handle
            smallest = min(smallest, nums[m])

            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m - 1

        return smallest