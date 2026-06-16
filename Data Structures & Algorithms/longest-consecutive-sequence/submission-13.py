# resolving since couldn't come up with optimal solution 1st time around

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        max_len = 1
        seen = set(nums)

        for _, v in enumerate(nums):
            # means this cannot be the start of a potential sequence
            if v - 1 in seen: 
                continue

            curr_len = 1
            curr_val = v
            while curr_val + 1 in seen:
                curr_len += 1
                curr_val += 1
            
            max_len = max(max_len, curr_len)
        
        return max_len