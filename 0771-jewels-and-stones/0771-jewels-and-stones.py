class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        f_map = {}
        res = 0

        for s in stones:
            if s in f_map:
                f_map[s] += 1
            else:
                f_map[s] = 1

        for j in jewels:
            if j in f_map:
                res += f_map[j]

        return res