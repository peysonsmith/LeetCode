class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)

        f = 0
        b = len(str_x) - 1

        if x >= 0:
            while f <= b:
                if str_x[f] != str_x[b]:
                    return False
                f += 1
                b -= 1

            return True

        return False
                