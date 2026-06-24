from collections import defaultdict

class Solution: 
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        freq = defaultdict(int)
        left, max_freq = 0, 0

        for right in range(len(s)):
            freq[s[right]] += 1
            if freq[s[right]] > max_freq:
                max_freq = freq[s[right]]

            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res