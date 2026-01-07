class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case
        if len(strs) == 1:
            return strs[0]

        # Find the minimum length
        min_len = 201
        for s in strs:
            min_len = min(min_len, len(s))

        # Index through each letter of each word until reached min length
        i = 0
        while i < min_len:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        
        return strs[0][:min_len]


            

        