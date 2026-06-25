from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 can be a permutation of itself so if its a substring of s2 return right away
        if s1 in s2:
            return True
        
        n, m = len(s1), len(s2)
        left = 0

        s1_freq = Counter(s1)

        for right in range(n - 1, m):
            curr_window_freq = Counter(s2[left:right+1])

            if curr_window_freq == s1_freq:
                return True
            
            left += 1
        
        return False