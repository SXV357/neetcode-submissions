class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 can be a permutation of itself so if its a substring of s2 return right away
        if s1 in s2:
            return True
        
        n, m = len(s1), len(s2)
        if n > m:
            return False

        s1_freq = [0] * 26
        for char in s1:
            s1_freq[ord(char) - 97] += 1
        
        # populating initial frequencies in window
        curr_window_freq = [0] * 26
        for i in range(n):
            curr_window_freq[ord(s2[i]) - 97] += 1

        left = 0
        for right in range(n - 1, m):
            if right > n - 1:
                curr_window_freq[ord(s2[right]) - 97] += 1

            if curr_window_freq == s1_freq:
                return True
            
            curr_window_freq[ord(s2[left]) - 97] -= 1
            left += 1
        
        return False