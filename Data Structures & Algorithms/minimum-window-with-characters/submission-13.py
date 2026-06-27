from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if n < m:
            return ""
        
        if m == 1:
            return t if t in s else ""
        
        if n == m and s == t:
            return t

        t_count = Counter(t)
        s_count = Counter()

        # copying same keys from t_count to s_count and initializing everything to 0
        for k in t_count:
            s_count[k] = 0

        # count we want to achieve vs what we begin with (will be updated as we move along)
        want = sum(t_count.values())
        need = 0

        min_len = float('inf')
        # the indices of the start and end of the substring meeting the conditions
        target_l, target_r = -1, -1

        left = 0
        for right in range(n):
            char = s[right]

            # doesn't contribute so we don't care
            if char not in s_count:
                continue
            
            # update it in s_count and if it equals what's in t_count update need
            s_count[char] += 1
            if s_count[char] <= t_count[char]:
                need += 1
            
            # we're not there yet
            if need != want:
                continue

            # keep removing chars until condition is violated
            while need == want:
                if right - left + 1 < min_len:
                    min_len = min(min_len, right - left + 1)
                    target_l, target_r = left, right
                
                curr_char = s[left]
                if curr_char in s_count:
                    s_count[curr_char] -= 1

                    if s_count[curr_char] < t_count[curr_char]:
                        need -= 1
                
                left += 1
        
        return s[target_l:target_r + 1]
