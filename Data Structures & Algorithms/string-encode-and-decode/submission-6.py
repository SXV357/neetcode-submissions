import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)

        built = ""

        for word in strs:
            wlen = str(len(word))
            built += f"{wlen}#{word}"
        
        return built

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#': j += 1
            wlen = int(s[i:j])

            words.append(s[j+1:j+1+wlen])
            i = j + 1 + wlen
        
        return words