# revisiting this since wasn't able to come up with good solution 1st time

'''
issue is since each strs[i] could be any of the 256 valid ascii chars
simply having a delimiter in between words is not enough because that
same delimiter could be present in an individual word itself breaking the solution

Even if I have just delimiter in front of each word I don't know how much to 
read after (I could read until next delim but breaks if words themselves 
have the same delimiter)

Need to have length encoded somehow so beyond using the delimiter I know
exactly how much to read after and even if the string has that same delim
I just read all of it
'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello", "World"] -> 5$Hello5$World
        encoded = ""

        for s in strs:
            n = len(s)
            encoded += f"{n}${s}"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        print(f"received s: {s}")
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            
            rlen = int(s[i:j])

            res.append(s[j + 1:j + 1 + rlen])
            i = j + 1 + rlen

        return res
