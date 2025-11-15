class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # Hashmap {key=open : val=closed}
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        # Add open parentheses to stack until it is closed
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        
        return False

        