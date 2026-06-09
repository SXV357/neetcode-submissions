class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        modified = sorted(list(set(nums)))

        largest, i = 1, 0
        cnt = 1
        while i < len(modified) - 1:
            curr, right = modified[i], modified[i + 1]
            if right > curr and right == curr + 1:
                cnt += 1
            elif right > curr and not right == curr + 1:
                cnt = 1
            
            largest = max(largest, cnt)
            
            i += 1
        
        return largest