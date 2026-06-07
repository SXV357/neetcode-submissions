# revisiting this since didn't come up with optimal solution 1st time itself

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        '''
        let n = len(strs)
        let m = avg length of strs[i]

        O(n * mlogm) - ok but not that efficient (we want to minimize sorting overhead)
        '''

        for s in strs:
            # m + m log m -> m log m
            arranged = tuple(sorted(s))

            if arranged not in dic:
                dic[arranged] = []
            
            dic[arranged].append(s)

        return list(dic.values())