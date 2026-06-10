class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        modified = set(nums)

        longest, cnt = 1, 1
        for val in nums:
            prev = val - 1

            # this value cannot be the start of a sequence
            if prev in modified:
                continue
            # means it is the start of a sequence
            else:
                temp = val + 1
                while temp in modified:
                    cnt += 1
                    temp += 1
                
                longest = max(longest, cnt)
                cnt = 1
        
        return longest
