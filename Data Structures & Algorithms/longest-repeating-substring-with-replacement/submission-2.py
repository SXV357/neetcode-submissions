# revisiting this problem since I 100% blanked out 1st time and had to watch NC video to solve it

from collections import defaultdict

class Solution:
    def get_most_freq_count(self, dic) -> int:
        max_freq = 0
        for v in dic.values():
            max_freq = max(max_freq, v)
        
        return max_freq

    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Caveat: self.get_most_freq_count is only O(26) since s only consists of 
        upper case english chars which effectively does resolve to O(1) but for more
        rigidity time complexity is O(26n) - O(n) is feasible and mainly involves manually
        tracking max_freq rather than re-computing everytime on the fly but its a small
        optimization which doesn't make a huge difference
        '''

        left = 0

        max_len = 0
        freq = defaultdict(int)
        for right in range(len(s)):
            freq[s[right]] += 1

            # premise is that in a given substring we wanna make characters equal the
            # most frequent one to get everything to be the same: number of chars to change
            # to make equal to most freq one is (window_size - frequency of most freq char)

            # we ideally want this to be under k since we can only replace up to k chars
            # if at all we do go over that's our window violation condition so we keep shrinking
            while (right - left + 1) - self.get_most_freq_count(freq) > k:
                freq[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len