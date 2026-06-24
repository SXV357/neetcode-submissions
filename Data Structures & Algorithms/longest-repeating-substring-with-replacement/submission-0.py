from collections import defaultdict

class Solution:
    def find_most_freq_char(self, dic) -> int:
        mk, mv = None, 0
        for k, v in dic.items():
            if v > mv:
                mv = v
                mk = k
        
        return mv        

    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        freq = defaultdict(int)
        left = 0
        for right in range(len(s)):
            freq[s[right]] += 1

            while (right - left + 1) - self.find_most_freq_char(freq) > k:
                freq[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res