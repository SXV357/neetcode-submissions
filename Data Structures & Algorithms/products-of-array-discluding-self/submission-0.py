class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        for i in range(n):
            prod = 1

            if i == 0:
                for j in range(1, n):
                    prod *= nums[j]
            elif i == n - 1:
                for j in range(0, n - 1):
                    prod *= nums[j]
            else:
                for j in range(0, i):
                    prod *= nums[j]
                
                for k in range(i + 1, n):
                    prod *= nums[k]
            
            res.append(prod)
        
        return res