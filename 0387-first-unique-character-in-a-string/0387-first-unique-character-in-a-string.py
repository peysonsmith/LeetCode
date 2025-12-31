class Solution:
    def firstUniqChar(self, s: str) -> int:
        f_map = {}

        for l in s:
            if l not in f_map:
                f_map[l] = 1
            else:
                f_map[l] += 1
        
        for i in range(len(s)):
            if f_map[s[i]] == 1:
                return i

        return -1