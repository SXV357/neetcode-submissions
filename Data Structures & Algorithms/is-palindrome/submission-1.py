class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified = s.lower()
        l, r = 0, len(modified) - 1

        while l < r:
            lc, rc = modified[l], modified[r]

            if not lc.isalnum():
                l += 1
                continue
            
            if not rc.isalnum():
                r -= 1
                continue
            
            if lc != rc:
                return False
            else:
                l += 1
                r -= 1
        
        return True