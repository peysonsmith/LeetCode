class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Convert string to lowercase
        lowerS = ""
        for i in range(len(s)):
            if s[i].isalnum():
                lowerS += s[i].lower()

        frontP = 0
        backP = len(lowerS) - 1

        for i in range(len(lowerS) // 2):
            if lowerS[frontP] != lowerS[backP]:
                return False
            else:
                frontP += 1
                backP -= 1

        return True