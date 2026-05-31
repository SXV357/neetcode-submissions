from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}

        for s in strs:
            counts = [0] * 26

            for char in s:
                counts[ord(char) - 97] += 1
            
            modified = tuple(counts)
            if modified not in groupings:
                groupings[modified] = []
            
            groupings[modified].append(s)
        
        return list(groupings.values())