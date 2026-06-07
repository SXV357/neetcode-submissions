# revisiting this since didn't come up with optimal solution 1st time itself

from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        '''
        let n = len(strs)
        let m = avg length of strs[i]

        below approach: O(n * m) which is big improvement but still relies on sorting
        '''

        for s in strs:
            # computing counts = O(m)
            counts = Counter(s)
            print(f"counts = {counts}")

            # sorting is O(26 log 26) => O(1)
            # converting to tuple for immutability in dictionary is O(26) => O(1)
            arranged = tuple(sorted(counts.items(), key = lambda x: x[0]))
            print(f"arranged: {arranged}")

            if arranged not in dic:
                dic[arranged] = []
            
            dic[arranged].append(s)

        return list(dic.values())