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
            SMap[s[i]] = 1 + SMap.get(s[i], 0)
            TMap[t[i]] = 1 + TMap.get(t[i], 0)

        for key in SMap:
            if key not in TMap:
                return False
            if SMap[key] != TMap[key]:
                return False

        return True