class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        leftP = 0
        rightP = len(s) - 1

        while leftP < rightP:
            while leftP < rightP and not s[leftP].isalnum():
                leftP += 1
            while leftP < rightP and not s[rightP].isalnum():
                rightP -= 1
            if s[leftP].lower() != s[rightP].lower():
                return False
            leftP += 1
            rightP -= 1

        return True

                