class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2 != 0):
            return False

        stack = []

        mapSet = {')' : '(', '}' : '{' , ']':'['}

        for char in s:
            if char in mapSet:
                if not stack or stack.pop() != mapSet[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack