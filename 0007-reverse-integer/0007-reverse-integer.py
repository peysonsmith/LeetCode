class Solution:
    def reverse(self, x: int) -> int:

        rev = str(x)[::-1]
        if rev[(len(rev) - 1)] == "-":
            rev = rev[:-1]
            rev = int(rev) * -1
        else:
            rev = int(rev)

        if rev > 2 ** 31 - 1 or rev < -2 ** 31:
            return 0
        return rev
