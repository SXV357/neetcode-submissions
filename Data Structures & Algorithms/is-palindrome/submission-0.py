class Solution:
    def isPalindrome(self, s: str) -> bool:
        built = ""
        for char in s:
            if char.isalnum():
                built += char.lower()
        
        l, r = 0, len(built) - 1
        while l < r:
            if built[l] != built[r]:
                return False
            
            l += 1
            r -= 1
        
        return True