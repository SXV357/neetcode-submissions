from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # attempt at optimized one
        n = len(nums)

        # will be used for computations
        prefix = [nums[0]]

        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])
        
        # print(f"prefix: {prefix}")
        
        '''
        prefix[r] - old prefix = k

        does below exist in hashmap?
        prefix[r] - k = old prefix
        '''

        mappings = defaultdict(int)
        mappings[0] = 1

        count = 0

        for right in range(n):
            curr = prefix[right]

            if curr - k in mappings:
                count += mappings[curr - k]
            
            mappings[curr] += 1

        return count