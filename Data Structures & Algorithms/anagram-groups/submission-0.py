class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}

        for s in strs:
            modified = ''.join(sorted(s))

            if modified not in groupings:
                groupings[modified] = []
            
            groupings[modified].append(s)
        
        return list(groupings.values())