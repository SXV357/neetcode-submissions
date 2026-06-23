from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        max_len, left = 0, 0

        for right in range(len(s)):
            freq[s[right]] += 1

            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len