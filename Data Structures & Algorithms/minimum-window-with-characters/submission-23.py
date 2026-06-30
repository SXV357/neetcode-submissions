# need to revisit this - wasnt able to come up with optimal solution though I figured out brute force
# to begin with (had to watch NC video to figure it out)

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)

        # base cases
        if m > n: return ""
        if (n == m and s == t) or (m == 1 and t in s): return t

        '''
        naive: for every substring in s, check if it contains same freq of chars as t
        and if so update min len as we check everything - O(n^2) which is very inefficient
        since string lengths can go as high as 1000
        '''

        t_freq = Counter(t)
        s_freq = Counter()

        # we only care about making entries for the same keys as exist in t_freq
        for k in t_freq:
            s_freq[k] = 0

        want = sum(t_freq.values())
        have = 0

        left = 0
        target_l, target_r = -1, -1
        min_len = float('inf')

        for right in range(n):
            char = s[right]

            # we don't care so can keep moving on
            if char not in s_freq: continue

            s_freq[char] += 1
            if s_freq[char] == t_freq[char]:
                have += s_freq[char]
            
            while have == want:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    target_l, target_r = left, right
                    
                curr = s[left]

                # again we don't care so skip
                if curr in s_freq:
                    s_freq[curr] -= 1

                    if s_freq[curr] < t_freq[curr]:
                        have -= t_freq[curr]

                # do this regardless
                left += 1
        
        return s[target_l:target_r + 1] if target_l < target_r else ""
                