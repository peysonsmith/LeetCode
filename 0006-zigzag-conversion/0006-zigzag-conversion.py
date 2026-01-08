class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if only 1 row or string shorter than rows, return as is
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]

        c = 0
        while c < len(s):
            for i in range(numRows):
                if c < len(s):
                    rows[i].append(s[c])
                    c += 1
            for i in range(numRows - 2, 0, -1):
                if c < len(s):
                    rows[i].append(s[c])
                    c += 1

        # Add all characters to set
        res = ""
        for row in rows:
            for c in row:
                res += c

        return res