class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Edge Case: If the lengths are different return false
        if len(s) != len(t):
            return False

        SMap = {}
        TMap = {}

        for i in range(len(s)):
            if s[i] in SMap:
                SMap[s[i]] += 1
            else:
                SMap[s[i]] = 1

        for i in range(len(t)):
            if t[i] in TMap:
                TMap[t[i]] += 1
            else:
                TMap[t[i]] = 1

        for key in SMap:
            if key not in TMap:
                return False
            if SMap[key] != TMap[key]:
                return False

        return True