# revisiting this just to try and implement prefix/postfix from scratch
# to get a better understanding (came up with O(n) division approach 
# first time around with no issues)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        '''
        prefix [1, 1, 2, 8]
        postfix [48, 24, 6, 1]
        '''

        prefix = [1] * n
        postfix = [1] * n

        # computing prefix
        start, prev = 1, nums[0]
        for i in range(1, n):
            start *= prev
            prefix[i] = start
            prev = nums[i]
        
        # computing postfix
        start, prev = 1, nums[-1]
        for i in range(n - 2, -1, -1):
            start *= prev
            postfix[i] = start
            prev = nums[i]
        
        res = []
        for i in range(n):
            res.append(prefix[i] * postfix[i])
        
        return res