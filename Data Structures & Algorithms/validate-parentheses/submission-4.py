class Solution:
    def isValid(self, s: str) -> bool:
        # purely the keys only??
        mappings = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []

        for char in s:
            if char not in mappings:
                stack.append(char)
            else:
                if (not stack) or (stack and stack[-1] != mappings[char]):
                    return False
                
                if stack and stack[-1] == mappings[char]:
                    stack.pop()
        
        return not stack
