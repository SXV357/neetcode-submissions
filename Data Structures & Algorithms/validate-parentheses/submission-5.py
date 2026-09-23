class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []

        for char in s:
            # opening brackets 
            if char not in mappings:
                stack.append(char)
            else:
                # we've encountered closing opening
                if not stack: return False

                if stack[-1] != mappings[char]:
                    return False
                
                stack.pop()
        
        return not stack