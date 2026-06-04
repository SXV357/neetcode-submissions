class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_count = nums.count(0)

        if zero_count == 0:
            res = []
            prod = 1
            for i in nums:
                prod *= i
            
            for j in nums:
                res.append(prod // j)
            
            return res
        elif zero_count == 1:
            idx = nums.index(0)
            res = [0] * n

            first, second = nums[:idx], nums[idx + 1:]
            prod = 1

            for val1 in first:
                prod *= val1
            
            for val2 in second:
                prod *= val2
            
            res[idx] = prod
            return res
        
        return [0] * n
            
