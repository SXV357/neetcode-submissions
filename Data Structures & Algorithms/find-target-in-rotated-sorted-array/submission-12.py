class Solution:
    def b_search(self, nums: list[int], target: int, l: int, r: int) -> int:
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1 
        
        return -1

    def search(self, nums: list[int], target: int) -> int:
        n = len(nums) - 1
        
        l, r = 0, n
        
        # already sorted so trivial
        if nums[l] <= nums[r]:
            return self.b_search(nums, target, 0, n)
        else:
            # rotated somewhere between 1 and n - 1 times
            
            # find min element first via binary search
            min_elem, min_idx = nums[0], 0
            l, r = 0, len(nums) - 1

            while l <= r:
                if nums[l] < nums[r]:
                    if nums[l] < min_elem:
                        min_elem = nums[l]
                        min_idx = l
                    break
                
                m = (l + r) // 2
                if nums[m] < min_elem:
                    min_elem = nums[m]
                    min_idx = m

                if nums[m] >= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
            first_sorted = self.b_search(nums, target, 0, min_idx - 1)
            second_sorted = self.b_search(nums, target, min_idx, n)
            
            if first_sorted != -1:
                return first_sorted
            if second_sorted != -1:
                return second_sorted
        
        return -1