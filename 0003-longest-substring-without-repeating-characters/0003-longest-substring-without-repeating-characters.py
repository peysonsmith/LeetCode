class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        maxLen = 0
        f = 0

        for b in range(len(s)):
            if s[b] not in letters:
                letters.add(s[b])
                maxLen = max(maxLen, (b-f + 1))
            else:
                while s[f] != s[b]:
                    letters.remove(s[f])
                    f += 1
                f += 1

        return maxLen