from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # optimized (sliding window)
        n, m = len(s1), len(s2)
        
        # keep this frozen
        s1_freq = Counter(s1)
        s2_freq = Counter()

        left = 0
        for right in range(m):
            curr = s2[right]

            s2_freq[curr] += 1

            if right - left + 1 == n:
                if s2_freq == s1_freq: 
                    return True
                else:
                    s2_freq[s2[left]] -= 1

                    if s2_freq[s2[left]] == 0:
                        s2_freq.pop(s2[left])
                        
                    left += 1

        return False

