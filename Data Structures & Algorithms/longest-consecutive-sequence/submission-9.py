class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        smallest = min(nums)
        largest = max(nums)

        max_len, cnt = 1, 1
        modified = set(nums)

        for val in range(smallest, largest + 1):
            curr_val, next_val = val, val + 1
            if curr_val in modified and next_val in modified:
                cnt += 1
            elif curr_val in modified and not next_val in modified:
                cnt = 1
            
            max_len = max(max_len, cnt)

        return max_len