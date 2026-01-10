class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        start = 0
        
        for i in range(len(chars) + 1):
            if i == len(chars) or chars[i] == ' ':
                left, right = start, i - 1
                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1
                start = i + 1
        
        return ''.join(chars)

        
            


            