# revisiting this since didn't come up with optimal solution 1st time itself

from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        '''
        let n = len(strs)
        let m = avg length of strs[i]

        now all count arrays are in deterministic order so no need to sort
        O(n * m)
        '''

        for s in strs:
            # O(26) -> O(1)
            counts = [0] * 26

            # O(m)
            for char in s:
                counts[ord(char) - 97] += 1
            
            # O(26) -> O(1)
            modified = tuple(counts)

            if modified not in dic:
                dic[modified] = []
            
            dic[modified].append(s)

        return list(dic.values())